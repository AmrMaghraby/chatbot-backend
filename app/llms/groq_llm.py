import os
import requests
from dotenv import load_dotenv
from app.llms.base import BaseLLM

load_dotenv()

class GroqClient(BaseLLM):
    API_URL = "https://api.groq.com/openai/v1/chat/completions"

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not set in environment variables.")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def chat(self, message: str, session_id: str, tools: dict):
        payload = {
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": message}]
        }

        try:
            response = requests.post(self.API_URL, json=payload, headers=self.headers)
            response.raise_for_status()
            content = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
            return {"message": content}
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {e}"}
        except Exception as e:
            return {"error": f"Unexpected error: {e}"}
