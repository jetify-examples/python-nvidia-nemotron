import os
from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("API_KEY")
)

def prompt(message: str) -> str:
  chat_completion = client.chat.completions.create(
    messages=[
      {
        "role": "user",
        "content": message,
      }
    ],
    model="nvidia/llama-3.1-nemotron-70b-instruct",
  )
  return chat_completion.choices[0].message
