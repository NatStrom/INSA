import asyncio
from pathlib import Path
from typing import Type
from itertools import batched  # python 3.12+

import httpx
import instructor
import openai
from instructor import AsyncInstructor
from pydantic import BaseModel

from models import ListedEntity


OPEN_AI_SEED = 42
CHUNK_DELIMITER = "\n\n"


class SanctionedEntities(BaseModel):
    entities: list[ListedEntity]


async def extract_entities(
    text: str,
    client: AsyncInstructor,
    response_model: Type[BaseModel],
):
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text},
        ],
        response_model=response_model,
        strict=False,
        max_retries=1,
        seed=OPEN_AI_SEED,
    )
    return response


async def process_batch(
    batch: list[str],
    client: AsyncInstructor,
) -> list[ListedEntity]:
    text = CHUNK_DELIMITER.join(batch)
    result: SanctionedEntities = await extract_entities(
        text, client, SanctionedEntities
    )
    return result.entities


async def process_chunks(
    chunks: list[str], client: AsyncInstructor, chunk_size: int = 5
) -> list[ListedEntity]:
    """synchronous processing of chunks"""
    all_entities = []
    for i, batch in enumerate(batched(chunks, chunk_size)):
        print(f"Processing batch {i+1} of {len(chunks)//chunk_size}")
        text = "\n\n".join(batch)
        result: SanctionedEntities = await extract_entities(
            text, client, SanctionedEntities
        )
        all_entities.extend(result.entities)
    return all_entities


async def main() -> None:
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=False, default="entities.json")
    args = parser.parse_args()

    client: AsyncInstructor = instructor.from_openai(
        openai.AsyncOpenAI(
            max_retries=5,
            timeout=30.0,  # total operation timeout
            http_client=httpx.AsyncClient(
                timeout=httpx.Timeout(connect=5.0, read=30.0, write=30.0, pool=30.0)
            ),
        ),
    )

    with open(args.input, "r", encoding="latin-1") as f:
        content = f.read()

    sections = content.split(CHUNK_DELIMITER)
    entities = await process_chunks(sections, client)

    records = [e.model_dump_json() for e in entities]
    with open(args.output, "w", encoding="utf-8") as f:
        for record in records:
            f.write(record)
            f.write("\n")


if __name__ == "__main__":
    asyncio.run(main())
