from dotenv import load_dotenv
load_dotenv()

from literalai import LiteralClient
from openai import OpenAI

literal_client = LiteralClient()
literal_client.instrument_openai()

openai_client = OpenAI()
