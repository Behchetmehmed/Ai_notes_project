from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam

client = OpenAI(api_key="YOUR_API_KEY_HERE")

topic = input("Въведи кратка идея")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        ChatCompletionUserMessageParam(
            content=f"Разшири тази идея в няколко изречения: {topic}"
        )
    ]
)

print(response.choices[0].message.content)