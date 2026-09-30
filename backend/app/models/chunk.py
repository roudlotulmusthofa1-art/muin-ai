from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class KitabChunk(BaseModel):
    chunk_id: str = Field(..., description="ID unik chunk, misal: fathul-qarib_p12_c1")
    kitab_id: str
    kitab_name: str
    muallif: str
    wafat_year: Optional[int] = None
    bidang: str = "Fikih"
    mazhab: str = "Syafi'i"
    kategori_sumber: str = "mutun"
    juz: int = 1
    halaman: int = 1
    bab: Optional[str] = None
    fasl: Optional[str] = None
    text_arabic: str = Field(..., description="Teks bahasa Arab asli dari PDF")
    text_clean: str = Field(..., description="Teks Arab yang sudah dinormalisasi tanpa harakat untuk pencarian BM25")
    metadata: Dict[str, Any] = Field(default_factory=dict)

class SearchResult(BaseModel):
    chunk: KitabChunk
    score: float = Field(0.0, description="Skor kecocokan gabungan BM25 + Dense Vector")
