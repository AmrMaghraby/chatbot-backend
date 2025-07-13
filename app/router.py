from fastapi import APIRouter
from pydantic import BaseModel
from app.llms.openai_llm import OpenAIClient
from app.llms.groq_llm import GroqClient
from app.tools.bank_tools import TOOL_FUNCTIONS

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    session_id: str
    model: str  # e.g. "gpt-4" or "llama3"

@router.post("/")
async def chat(req: ChatRequest):
    if req.model == "gpt-4":
        client = OpenAIClient()
    elif req.model == "llama3":
        client = GroqClient()
    else:
        return {"error": "Unsupported model"}

    return await client.chat(req.message, req.session_id, TOOL_FUNCTIONS)

# ✅ This line is required for the import to work
chat_router = router
