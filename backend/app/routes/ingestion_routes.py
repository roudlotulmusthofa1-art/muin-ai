from fastapi import APIRouter, UploadFile, File, Form
from ..controllers import ingestion_controller

router = APIRouter(prefix="/ingestion", tags=["PDF Ingestion"])

@router.post("/upload", summary="Unggah dan indeks file PDF kitab baru")
async def upload_kitab_pdf(
    file: UploadFile = File(...),
    kitab_id: str = Form(...),
    kitab_name: str = Form(...),
    muallif: str = Form(...),
    wafat_year: int = Form(None),
    mazhab: str = Form("Syafi'i"),
    bidang: str = Form("Fikih"),
    kategori_sumber: str = Form("mutun")
):
    return await ingestion_controller.upload(
        file=file,
        kitab_id=kitab_id,
        kitab_name=kitab_name,
        muallif=muallif,
        wafat_year=wafat_year,
        mazhab=mazhab,
        bidang=bidang,
        kategori_sumber=kategori_sumber
    )
