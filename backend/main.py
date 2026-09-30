import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings, DatabaseManager
from app.routes import api_router

# Setup logger
logging.basicConfig(
    level=logging.INFO if settings.APP_DEBUG else logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

# Inisialisasi FastAPI App
app = FastAPI(
    title=settings.APP_NAME,
    description="Backend Engine Riset Fikih & Tafsir Muin AI berbasis RAG Kitab Turats & 9Router Gateway",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware (agar frontend Vue dapat memanggil backend secara aman)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Daftarkan Router API (seperti routes/api.php)
app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    logger.info("Memulai %s...", settings.APP_NAME)
    DatabaseManager.ensure_directories()
    # Inisialisasi koneksi awal ke Qdrant
    DatabaseManager.get_qdrant()
    logger.info("Backend siap melayani permintaan riset.")

@app.get("/")
async def root():
    return {
        "app": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "api_docs": "/docs",
        "api_v1": "/api/v1"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.APP_DEBUG
    )
