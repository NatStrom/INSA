
## Extract sanctioned entities 

This directory is an experimental implementation of the entity extraction process using Pydantic and OpenAI's GPT-4o model.

Ensure Python 3.12 is installed, create a virtual environment and install the dependencies with `pip install -r requirements.txt`. Ensure the OpenAI API key is set in the environment variable `OPENAI_API_KEY`.

Run the script with `python main.py --input_file <path to input file> --output_file <path to output file>`.

The input file is assumed to be raw text, not HTML.
