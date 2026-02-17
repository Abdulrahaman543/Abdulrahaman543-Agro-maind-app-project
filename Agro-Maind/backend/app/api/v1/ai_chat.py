from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.ai_service import AIService

router = APIRouter()
ai_service = AIService()

class ChatRequest(BaseModel):
    user_id: str
    message: str
    language: str = "en"

class ChatResponse(BaseModel):
    response: str

@router.post("/chat/text", response_model=ChatResponse)
async def chat_text(request: ChatRequest):
    try:
        response = await ai_service.process_text(request.user_id, request.message, request.language)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat/voice", response_model=ChatResponse)
async def chat_voice(request: ChatRequest):
    try:
        response = await ai_service.process_voice(request.user_id, request.message, request.language)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))