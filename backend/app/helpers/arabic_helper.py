import re

# Karakter harakat/diakritik Arab (Unicode range U+064B - U+065F, plus tatweel & dagger alif)
ARABIC_DIACRITICS = re.compile(r"[\u064B-\u0652\u0656-\u065F\u0670\u0640]")

def remove_tashkeel(text: str) -> str:
    """Menghilangkan harakat, tanwin, sukun, syaddah, dan tatweel dari teks Arab"""
    if not text:
        return ""
    return ARABIC_DIACRITICS.sub("", text)

def normalize_arabic(text: str) -> str:
    """Menormalisasi bentuk huruf Arab untuk memudahkan pencarian kata kunci (BM25 / regex)
    - Menyatukan berbagai bentuk alif (أ, إ, آ, ٱ -> ا)
    - Menyatukan alif maqshurah dan yaa (ى -> ي)
    - Menyatukan taa marbuthah (ة -> ه)
    """
    if not text:
        return ""
    text = remove_tashkeel(text)
    text = re.sub(r"[إأآٱ]", "ا", text)
    text = re.sub(r"ى", "ي", text)
    text = re.sub(r"ة", "ه", text)
    # Hapus spasi berlebih
    text = re.sub(r"\s+", " ", text).strip()
    return text

def contains_arabic(text: str) -> bool:
    """Mengecek apakah string mengandung karakter huruf Arab"""
    return bool(re.search(r"[\u0600-\u06FF]", text))
