import logging
import os
from typing import Optional
from qdrant_client import QdrantClient
from .settings import settings

logger = logging.getLogger(__name__)

class DatabaseManager:
    _qdrant_client: Optional[QdrantClient] = None

    @classmethod
    def get_qdrant(cls) -> QdrantClient:
        """Mendapatkan client Qdrant singleton, dengan in-memory fallback jika server belum aktif"""
        if cls._qdrant_client is None:
            try:
                if settings.QDRANT_HOST and settings.QDRANT_HOST != ":memory:":
                    cls._qdrant_client = QdrantClient(
                        host=settings.QDRANT_HOST,
                        port=settings.QDRANT_PORT,
                        api_key=settings.QDRANT_API_KEY or None,
                        timeout=5.0
                    )
                    # Cek konektivitas
                    cls._qdrant_client.get_collections()
                    logger.info("Terhubung ke Qdrant server di %s:%s", settings.QDRANT_HOST, settings.QDRANT_PORT)
                else:
                    cls._qdrant_client = QdrantClient(":memory:")
                    logger.info("Menggunakan Qdrant in-memory mode")
            except Exception as e:
                logger.warning("Gagal terhubung ke Qdrant server (%s). Fallback ke in-memory mode.", e)
                cls._qdrant_client = QdrantClient(":memory:")
        return cls._qdrant_client

    @classmethod
    def ensure_directories(cls):
        """Memastikan folder storage fisik tersedia"""
        os.makedirs(settings.PDF_STORAGE_DIR, exist_ok=True)
        os.makedirs(settings.EXTRACTED_STORAGE_DIR, exist_ok=True)
