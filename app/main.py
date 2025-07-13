from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import chat_router

app = FastAPI(title="LLM-Agnostic Chatbot")

origins = [
    "http://localhost:5173",
    "https://chatbot-frontend-nkqapod1t-amrmaghrabys-projects.vercel.app",
    "https://chatbot-frontend-git-main-amrmaghrabys-projects.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your API
app.include_router(chat_router, prefix="/chat")
