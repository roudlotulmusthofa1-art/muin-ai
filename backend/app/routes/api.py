from fastapi import APIRouter
from .chat_routes import router as chat_router
from .kitab_routes import router as kitab_router
from .source_routes import router as source_router
from .ingestion_routes import router as ingestion_router

# Router utama untuk API v1 (seperti routes/api.php di Laravel)
api_router = APIRouter(prefix="/api/v1")

api_router.include_router(chat_router)
api_router.include_router(kitab_router)
api_router.include_router(source_router)
api_router.include_router(ingestion_router)

@api_router.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "service": "Muin AI Backend Engine",
        "version": "1.0.0"
    }
