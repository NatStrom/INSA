import asyncio
import json
from datetime import date, datetime
from pathlib import Path
from typing import Type

import httpx
import instructor
import openai
from instructor import AsyncInstructor
from pydantic import BaseModel

from models import ListedEntity


OPEN_AI_SEED = 42


class SanctionedEntities(BaseModel):
    entities: list[ListedEntity]
    )


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

    sections = content.split("\n\n")
    sections = sections[:5]
    text = "\n\n".join(sections)

    result: SanctionedEntities = await extract_entities(
        text, client, SanctionedEntities
    )

    records = [e.model_dump_json() for e in result.entities]
    with open(args.output, "w", encoding="utf-8") as f:
        for record in records:
            f.write(record)
            f.write("\n")


if __name__ == "__main__":
    asyncio.run(main())
