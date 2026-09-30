from typing import Optional

def format_citation(
    kitab_name: str,
    muallif: str,
    wafat_year: Optional[int] = None,
    juz: Optional[int] = None,
    halaman: Optional[int] = None,
    bab: Optional[str] = None
) -> str:
    """Format sitasi ilmiah standar pesantren & akademisi Islam
    Contoh: Fathul Mu'in bi Syarh Qurratil 'Ain, karya Zainuddin Al-Malibari (w. 987 H), Juz 1, Hal. 45
    """
    parts = [kitab_name]
    
    author_part = f"karya {muallif}"
    if wafat_year:
        author_part += f" (w. {wafat_year} H)"
    parts.append(author_part)

    if juz:
        parts.append(f"Juz {juz}")
    if halaman:
        parts.append(f"Hal. {halaman}")
    if bab:
        parts.append(f"[{bab}]")

    return ", ".join(parts)
