from config import openai_client
from bar import bar

def foo():
    response = openai_client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant."}])
    bar()