import logging
from fastapi import Request
from sse_starlette.sse import EventSourceResponse
from ..models import ChatRequest, ChatResponse
from ..services import rag_service
from ..helpers import success_response, error_response

logger = logging.getLogger(__name__)

class ChatController:
    """Controller penangan endpoint pertanyaan riset fikih & tafsir"""

    @staticmethod
    async def ask(request: ChatRequest):
        try:
            response: ChatResponse = await rag_service.answer_question(request)
            return success_response(
                data=response.dict(),
                message="Jawaban riset berhasil dihasilkan berbasis kitab sumber"
            )
        except Exception as e:
            logger.error("Error pada ChatController.ask: %s", e)
            return error_response(
                message=f"Terjadi kesalahan saat memproses riset: {str(e)}",
                status_code=500
            )

    @staticmethod
    async def ask_stream(request: ChatRequest):
        """Streaming response SSE untuk jawaban panjang realtime"""
        async def event_generator():
            try:
                response = await rag_service.answer_question(request)
                # Kirim metadata rujukan & ibarah pertama
                yield {
                    "event": "citations",
                    "data": [c.dict() for c in response.citations]
                }
                # Kirim token jawaban
                chunk_size = 20
                for i in range(0, len(response.answer), chunk_size):
                    yield {
                        "event": "message",
                        "data": response.answer[i:i+chunk_size]
                    }
                yield {
                    "event": "done",
                    "data": "[COMPLETED]"
                }
            except Exception as e:
                yield {
                    "event": "error",
                    "data": str(e)
                }

        return EventSourceResponse(event_generator())

chat_controller = ChatController()
