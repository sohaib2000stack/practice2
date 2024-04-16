from fastapi import APIRouter
from .chatbot import router as chatbot_router

api_router = APIRouter()
api_router.include_router(chatbot_router)


# from .chatbot import router as chatbot_router







