from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Citation(BaseModel):
    kitab_id: str = Field(..., description="ID unik kitab")
    kitab_name: str = Field(..., description="Nama resmi kitab")
    muallif: str = Field(..., description="Nama pengarang / ulama")
    wafat_year: Optional[int] = Field(None, description="Tahun wafat mu'allif (Hijriyah)")
    juz: Optional[int] = Field(None, description="Nomor jilid / juz")
    halaman: Optional[int] = Field(None, description="Nomor halaman")
    bab: Optional[str] = Field(None, description="Bab pembahasan")
    fasl: Optional[str] = Field(None, description="Fasl pembahasan")
    ibarah_arab: str = Field(..., description="Kutipan ibarah Arab asli dari halaman fisik kitab")
    relevance_score: float = Field(0.0, description="Tingkat relevansi retrieval (0-1)")

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=2, description="Pertanyaan riset pengguna")
    scope: str = Field("fikih-syafii-riset", description="Scope fann/kajian (fikih-syafii-riset, fikih-syafii-ibarah, ushul-fikih, tafsir)")
    source: str = Field("auto", description="Kategori sumber (auto, mutun, fatawa, kontemporer)")
    selected_kitab_ids: Optional[List[str]] = Field(default=None, description="Daftar ID kitab spesifik jika user memilih kitab tertentu")
    only_selected_sources: bool = Field(False, description="Jika true, hanya rujuk sumber yang dipilih, tahan kesimpulan jika tidak ada")
    stream: bool = Field(False, description="Apakah menggunakan Server-Sent Events (SSE) streaming")

class ChatResponse(BaseModel):
    question: str
    scope: str
    source: str
    answer: str = Field(..., description="Penjelasan komprehensif atas masalah yang ditanyakan")
    ibarah: Optional[str] = Field(None, description="Ibarah Arab utama pendukung fatwa/hukum")
    citations: List[Citation] = Field(default_factory=list, description="Daftar rujukan dan ibarah yang dapat diverifikasi")
    model_used: Optional[str] = Field("9router/default", description="Model AI yang merespons via 9Router")
    created_at: datetime = Field(default_factory=datetime.utcnow)
