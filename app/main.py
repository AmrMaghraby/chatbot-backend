from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import chat_router

app = FastAPI(title="LLM-Agnostic Chatbot")

# Your API
app.include_router(chat_router, prefix="/chat")
