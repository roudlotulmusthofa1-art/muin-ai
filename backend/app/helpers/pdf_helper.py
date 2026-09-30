import os
import fitz  # PyMuPDF
from typing import List, Dict, Any

def extract_text_from_pdf(pdf_path: str) -> List[Dict[str, Any]]:
    """Mengekstrak teks per halaman dari file PDF kitab menggunakan PyMuPDF.
    Mengembalikan list dictionary: [{'page': 1, 'text': '...'}, ...]
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File PDF tidak ditemukan di: {pdf_path}")

    doc = fitz.open(pdf_path)
    pages = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text").strip()
        pages.append({
            "page": page_num + 1,
            "text": text,
            "is_empty": len(text) == 0
        })

    doc.close()
    return pages

def is_scanned_pdf(pages: List[Dict[str, Any]], sample_size: int = 5) -> bool:
    """Mendeteksi apakah PDF kemungkinan besar pindaian/scan (tidak ada layer teks digital)"""
    sample = pages[:min(sample_size, len(pages))]
    if not sample:
        return True
    empty_count = sum(1 for p in sample if p["is_empty"] or len(p["text"]) < 20)
    return empty_count >= (len(sample) * 0.8)
