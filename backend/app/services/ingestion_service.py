import os
import json
import logging
from typing import List, Dict, Any, Optional
from ..config import settings
from ..models import KitabChunk, KitabItem
from ..helpers import extract_text_from_pdf, is_scanned_pdf, normalize_arabic
from .vector_service import vector_service
from .rag_service import rag_service

logger = logging.getLogger(__name__)

class IngestionService:
    """Service untuk memproses file PDF kitab turats/tafsir, ekstraksi teks, dan indexing RAG"""

    def __init__(self):
        self.pdf_dir = settings.PDF_STORAGE_DIR
        self.extracted_dir = settings.EXTRACTED_STORAGE_DIR
        os.makedirs(self.pdf_dir, exist_ok=True)
        os.makedirs(self.extracted_dir, exist_ok=True)

    async def ingest_pdf(
        self,
        file_path: str,
        kitab_info: KitabItem,
        chunk_page_interval: int = 1
    ) -> Dict[str, Any]:
        """Memproses satu file PDF kitab dan mengindeksnya ke Vector DB dan BM25"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File PDF tidak ditemukan: {file_path}")

        logger.info("Memulai ekstraksi PDF kitab: %s (%s)", kitab_info.name, file_path)
        pages = extract_text_from_pdf(file_path)

        if is_scanned_pdf(pages):
            logger.warning("Kitab %s terdeteksi sebagai PDF pindaian (scan image). Perlu OCR.", kitab_info.name)

        chunks: List[KitabChunk] = []

        for p in pages:
            raw_text = p["text"]
            if not raw_text or len(raw_text.strip()) < 10:
                continue

            clean_text = normalize_arabic(raw_text)
            chunk_id = f"{kitab_info.id}_p{p['page']}"

            chunk = KitabChunk(
                chunk_id=chunk_id,
                kitab_id=kitab_info.id,
                kitab_name=kitab_info.name,
                muallif=kitab_info.muallif,
                wafat_year=kitab_info.wafat_year,
                bidang=kitab_info.bidang,
                mazhab=kitab_info.mazhab,
                kategori_sumber=kitab_info.kategori_sumber,
                juz=1,
                halaman=p["page"],
                text_arabic=raw_text,
                text_clean=clean_text,
                metadata={
                    "total_pages": len(pages),
                    "file_name": os.path.basename(file_path)
                }
            )
            chunks.append(chunk)

        # 1. Simpan ke Vector DB
        if chunks:
            await vector_service.upsert_chunks(chunks)
            # 2. Tambah ke BM25 Corpus
            rag_service.add_chunks_to_corpus(chunks)

            # 3. Simpan checkpoint JSON ke storage/extracted
            checkpoint_file = os.path.join(self.extracted_dir, f"{kitab_info.id}_extracted.json")
            with open(checkpoint_file, "w", encoding="utf-8") as f:
                json.dump([ch.dict() for ch in chunks], f, ensure_ascii=False, indent=2)

        return {
            "kitab_id": kitab_info.id,
            "kitab_name": kitab_info.name,
            "total_pages": len(pages),
            "indexed_chunks": len(chunks),
            "status": "completed"
        }

ingestion_service = IngestionService()
