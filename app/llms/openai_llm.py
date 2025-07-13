import os
import json
import openai
from dotenv import load_dotenv
from app.llms.base import BaseLLM

load_dotenv()

class OpenAIClient(BaseLLM):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set in environment variables.")
        openai.api_key = self.api_key

    def _format_functions(self, tools: dict) -> list:
        """Generate OpenAI tool definitions from Python functions."""
        formatted = []
        for name, func in tools.items():
            arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
            formatted.append({
                "name": name,
                "description": func.__doc__ or name,
                "parameters": {
                    "type": "object",
                    "properties": {key: {"type": "string"} for key in arg_names},
                    "required": list(arg_names)
                }
            })
        return formatted

    async def chat(self, message: str, session_id: str, tools: dict):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "user", "content": message}],
                functions=self._format_functions(tools),
                function_call="auto"
            )

            output = response.choices[0].message

            if output.get("function_call"):
                fn_name = output["function_call"]["name"]
                arguments = json.loads(output["function_call"]["arguments"])
                if fn_name in tools:
                    result = tools[fn_name](**arguments)
                    return {"tool_call": fn_name, "arguments": arguments, "result": result}

            return {"message": output.get("content")}
        except Exception as e:
            return {"error": f"OpenAI request failed: {e}"}
