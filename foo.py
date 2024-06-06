from config import literal_client, openai_client


@literal_client.step(type="run")
def foo():
    literal_client.message(content="Hello from foo!")
    response = openai_client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant."}])
    literal_client.message(content=response.choices[0].message.content)
    response = openai_client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant."}])
    literal_client.message(content=response.choices[0].message.content)
