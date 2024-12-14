import os
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()


class GPTClientMain:
    def __init__(self, api_key, model="gpt-4o-2024-08-06"):
        client.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model

    async def call_gpt(self, messages, response_format):
        try:
            response = client.beta.chat.completions.parse(
                model=self.model,
                messages=messages,
                response_format=response_format,
            )
            return response.choices[0].message.parsed
        except Exception as e:
            raise RuntimeError(f"Failed to call GPT API: {str(e)}")


class GPTClientOutput:
    def __init__(self, api_key, model="gpt-4o-mini-2024-07-18"):
        client.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model

    async def call_gpt(self, messages, response_format):
        try:
            response = client.beta.chat.completions.parse(
                model=self.model,
                messages=messages,
                response_format=response_format,
            )
            return response.choices[0].message.parsed
        except Exception as e:
            raise RuntimeError(f"Failed to call GPT API: {str(e)}")
