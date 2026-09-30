import logging
import hashlib
from typing import List, Dict, Any, Optional
from qdrant_client import models as qmodels
from ..config import settings, DatabaseManager
from ..models import KitabChunk

logger = logging.getLogger(__name__)

class VectorService:
    """Service untuk interaksi dengan Qdrant Vector Store untuk teks kitab turats"""

    def __init__(self):
        self.collection_name = settings.QDRANT_COLLECTION
        self.dimension = settings.EMBEDDING_DIMENSION
        self._ensure_collection()

    def _get_client(self):
        return DatabaseManager.get_qdrant()

    def _ensure_collection(self):
        try:
            client = self._get_client()
            collections = client.get_collections().collections
            exists = any(c.name == self.collection_name for c in collections)
            if not exists:
                client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=qmodels.VectorParams(
                        size=self.dimension,
                        distance=qmodels.Distance.COSINE
                    )
                )
                logger.info("Collection Qdrant '%s' berhasil dibuat.", self.collection_name)
        except Exception as e:
            logger.warning("Belum dapat memastikan collection Qdrant: %s", e)

    def _mock_embedding(self, text: str) -> List[float]:
        """Menghasilkan deterministic vector embedding untuk development lokal tanpa API key"""
        hasher = hashlib.sha256(text.encode("utf-8")).digest()
        # Buat array float panjang self.dimension dari hash
        vector = []
        for i in range(self.dimension):
            byte_val = hasher[i % len(hasher)]
            val = ((byte_val / 255.0) * 2.0) - 1.0
            vector.append(float(val))
        # Normalisasi
        norm = sum(x * x for x in vector) ** 0.5 or 1.0
        return [x / norm for x in vector]

    async def get_embedding(self, text: str) -> List[float]:
        """Mendapatkan vector embedding (via OpenAI atau deterministic fallback jika offline)"""
        if settings.OPENAI_API_KEY:
            try:
                import httpx
                async with httpx.AsyncClient(timeout=30.0) as client:
                    resp = await client.post(
                        "https://api.openai.com/v1/embeddings",
                        headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
                        json={"input": text, "model": settings.EMBEDDING_MODEL}
                    )
                    resp.raise_for_status()
                    return resp.json()["data"][0]["embedding"]
            except Exception as e:
                logger.warning("Gagal fetch OpenAI embedding (%s), memakai mock embedding.", e)
        return self._mock_embedding(text)

    async def upsert_chunks(self, chunks: List[KitabChunk]):
        """Menyimpan batch chunk ke dalam Qdrant"""
        client = self._get_client()
        points = []

        for i, ch in enumerate(chunks):
            embedding = await self.get_embedding(ch.text_clean or ch.text_arabic)
            points.append(
                qmodels.PointStruct(
                    id=abs(hash(ch.chunk_id)) % (10**12),
                    vector=embedding,
                    payload=ch.dict()
                )
            )

        client.upsert(
            collection_name=self.collection_name,
            points=points
        )
        logger.info("%d chunk kitab berhasil disimpan ke Qdrant", len(points))

    async def search(
        self,
        query: str,
        limit: int = 5,
        kitab_ids: Optional[List[str]] = None,
        mazhab: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Mencari chunk kitab yang paling relevan secara semantik"""
        client = self._get_client()
        query_vector = await self.get_embedding(query)

        # Filter metadata
        conditions = []
        if kitab_ids:
            conditions.append(
                qmodels.FieldCondition(
                    key="kitab_id",
                    match=qmodels.MatchAny(any=kitab_ids)
                )
            )
        if mazhab:
            conditions.append(
                qmodels.FieldCondition(
                    key="mazhab",
                    match=qmodels.MatchValue(value=mazhab)
                )
            )

        query_filter = qmodels.Filter(must=conditions) if conditions else None

        results = client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            query_filter=query_filter,
            limit=limit
        )

        output = []
        for r in results:
            output.append({
                "score": float(r.score),
                "payload": r.payload
            })
        return output

vector_service = VectorService()
