from fastapi import APIRouter
from ..models import ChatRequest
from ..controllers import chat_controller

router = APIRouter(prefix="/chat", tags=["Chat & Riset"])

@router.post("/ask", summary="Kirim pertanyaan riset fiqih / tafsir")
async def ask_question(request: ChatRequest):
    return await chat_controller.ask(request)

@router.post("/stream", summary="Streaming jawaban riset realtime via Server-Sent Events (SSE)")
async def ask_question_stream(request: ChatRequest):
    return await chat_controller.ask_stream(request)
