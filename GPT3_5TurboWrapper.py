from openai import OpenAI
import os

class GPT3_5TurboWrapper:
    def __init__(self):
        # Fetches the API key from the environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is not set in environment variables")
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),
)

    def predict(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            max_tokens=50,
            temperature=0.7)
        return response.choices[0].message.content
