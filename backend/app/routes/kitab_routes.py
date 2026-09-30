from typing import Optional
from fastapi import APIRouter, Query
from ..controllers import kitab_controller

router = APIRouter(prefix="/kitabs", tags=["Kitab Turats"])

@router.get("", summary="Dapatkan seluruh daftar kitab yang tersedia")
async def get_kitabs(
    bidang: Optional[str] = Query(None, description="Filter bidang: Fikih, Tafsir, Ushul Fikih"),
    mazhab: Optional[str] = Query(None, description="Filter mazhab: Syafi'i, Hanafi, dll.")
):
    return await kitab_controller.index(bidang=bidang, mazhab=mazhab)

@router.get("/{kitab_id}", summary="Dapatkan detail metadata spesifik kitab")
async def get_kitab(kitab_id: str):
    return await kitab_controller.show(kitab_id)
