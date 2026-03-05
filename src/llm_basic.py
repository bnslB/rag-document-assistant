from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that explains AI concepts simply."},
        {"role": "user", "content": "Explain tokens, embeddings, context window, and temperature in LLMs."}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)