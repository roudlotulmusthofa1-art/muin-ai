import os
import shutil
from fastapi import UploadFile, Form
from ..models import KitabItem
from ..services import ingestion_service
from ..config import settings
from ..helpers import success_response, error_response

class IngestionController:
    """Controller untuk menangani upload file PDF kitab baru dan memulai indexing"""

    @staticmethod
    async def upload(
        file: UploadFile,
        kitab_id: str = Form(...),
        kitab_name: str = Form(...),
        muallif: str = Form(...),
        wafat_year: int = Form(None),
        mazhab: str = Form("Syafi'i"),
        bidang: str = Form("Fikih"),
        kategori_sumber: str = Form("mutun")
    ):
        if not file.filename.lower().endswith(".pdf"):
            return error_response(message="Hanya file berekstensi .pdf yang diperbolehkan", status_code=400)

        # Simpan file ke storage/pdfs
        os.makedirs(settings.PDF_STORAGE_DIR, exist_ok=True)
        dest_path = os.path.join(settings.PDF_STORAGE_DIR, f"{kitab_id}_{file.filename}")

        with open(dest_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Siapkan metadata kitab
        kitab_info = KitabItem(
            id=kitab_id,
            name=kitab_name,
            muallif=muallif,
            wafat_year=wafat_year,
            mazhab=mazhab,
            bidang=bidang,
            kategori_sumber=kategori_sumber
        )

        # Jalankan proses ekstraksi dan indexing
        result = await ingestion_service.ingest_pdf(dest_path, kitab_info)

        return success_response(
            data=result,
            message=f"Kitab '{kitab_name}' berhasil diunggah dan terindeks ke database riset"
        )

ingestion_controller = IngestionController()
