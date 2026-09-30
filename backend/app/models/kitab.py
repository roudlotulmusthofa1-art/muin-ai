from typing import List, Optional
from pydantic import BaseModel, Field

class KitabItem(BaseModel):
    id: str = Field(..., description="ID slug kitab, misal: fathul-qarib")
    name: str = Field(..., description="Nama kitab, misal: Fathul Qarib Al-Mujib")
    muallif: str = Field(..., description="Nama mu'allif, misal: Ibnu Qasim Al-Ghazi")
    wafat_year: Optional[int] = Field(None, description="Tahun wafat Hijriyah, misal: 918")
    mazhab: str = Field("Syafi'i", description="Mazhab/aliran, misal: Syafi'i, Hanafi")
    bidang: str = Field("Fikih", description="Bidang ilmu: Fikih, Ushul Fikih, Tafsir")
    kategori_sumber: str = Field("mutun", description="mutun, fatawa, atau kontemporer")
    total_pages: int = Field(0, description="Total halaman yang terindeks")
    is_available: bool = Field(True, description="Status ketersediaan file PDF")
    description: Optional[str] = Field(None, description="Deskripsi singkat kitab")

class ResearchFieldGroup(BaseModel):
    name: str = Field(..., description="Label grup bidang, misal: Fikih · Syafi'i")
    description: str = Field(..., description="Keterangan grup, misal: Urutan mu'allif berdasarkan tahun wafat")
    books: str = Field(..., description="Ringkasan ketersediaan, misal: 6 dari 8 kitab")
    status: str = Field("active", description="active | inactive | warning")
    open: bool = Field(False, description="State accordion terbuka/tertutup")
    items: List[KitabItem] = Field(default_factory=list, description="Daftar kitab dalam grup ini")
