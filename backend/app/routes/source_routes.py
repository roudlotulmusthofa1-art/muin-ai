from fastapi import APIRouter
from ..controllers import source_controller

router = APIRouter(prefix="/sources", tags=["Sumber Penelitian"])

@router.get("/fields", summary="Dapatkan taksonomi bidang, mazhab, dan kitab untuk panel riset")
async def get_research_fields():
    return await source_controller.get_research_fields()
