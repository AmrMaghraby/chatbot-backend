from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    async def chat(self, message: str, session_id: str, tools: dict):
        pass
