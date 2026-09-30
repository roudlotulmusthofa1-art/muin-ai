from typing import Optional
from ..models import KitabItem
from ..helpers import success_response

# Mock database daftar kitab turats mu'tabar
STORED_KITABS = [
    KitabItem(
        id="fathul-qarib",
        name="Fathul Qarib Al-Mujib",
        muallif="Ibnu Qasim Al-Ghazi",
        wafat_year=918,
        mazhab="Syafi'i",
        bidang="Fikih",
        kategori_sumber="mutun",
        total_pages=180,
        is_available=True,
        description="Syarah ringkas atas Matan At-Taqrib karya Al-Qadhi Abu Syuja'"
    ),
    KitabItem(
        id="fathul-muin",
        name="Fathul Mu'in bi Syarh Qurratil 'Ain",
        muallif="Zainuddin Al-Malibari",
        wafat_year=987,
        mazhab="Syafi'i",
        bidang="Fikih",
        kategori_sumber="mutun",
        total_pages=320,
        is_available=True,
        description="Syarah komprehensif fikih Syafi'i standar pesantren besar"
    ),
    KitabItem(
        id="safinatun-naja",
        name="Safinatun Naja",
        muallif="Salim bin Sumair Al-Hadhrami",
        wafat_year=1271,
        mazhab="Syafi'i",
        bidang="Fikih",
        kategori_sumber="mutun",
        total_pages=40,
        is_available=True,
        description="Matan fikih ibadah dasar mazhab Syafi'i"
    ),
    KitabItem(
        id="minhaj-at-thalibin",
        name="Minhajut Thalibin wa 'Umdatul Muftin",
        muallif="Imam An-Nawawi",
        wafat_year=676,
        mazhab="Syafi'i",
        bidang="Fikih",
        kategori_sumber="mutun",
        total_pages=450,
        is_available=True,
        description="Pilar utama fatwa muta'akhkhirin mazhab Syafi'i"
    ),
    KitabItem(
        id="tafsir-ibn-katsir",
        name="Tafsir Al-Qur'an Al-'Azhim",
        muallif="Ibnu Katsir Ad-Dimasyqi",
        wafat_year=774,
        mazhab="Jumhur",
        bidang="Tafsir",
        kategori_sumber="mutun",
        total_pages=2400,
        is_available=True,
        description="Tafsir bil ma'tsur paling terkenal dan komprehensif"
    ),
    KitabItem(
        id="tafsir-al-jalalain",
        name="Tafsir Al-Jalalain",
        muallif="Jalaluddin Al-Mahalli & Jalaluddin As-Suyuthi",
        wafat_year=911,
        mazhab="Syafi'i",
        bidang="Tafsir",
        kategori_sumber="mutun",
        total_pages=600,
        is_available=True,
        description="Tafsir ringkas padat yang sangat populer di pesantren"
    )
]

class KitabController:
    """Controller untuk menampilkan daftar kitab, mu'allif, dan fann"""

    @staticmethod
    async def index(bidang: Optional[str] = None, mazhab: Optional[str] = None):
        results = STORED_KITABS
        if bidang:
            results = [k for k in results if k.bidang.lower() == bidang.lower()]
        if mazhab:
            results = [k for k in results if k.mazhab.lower() == mazhab.lower()]

        return success_response(
            data=[k.dict() for k in results],
            message="Daftar kitab berhasil dimuat"
        )

    @staticmethod
    async def show(kitab_id: str):
        found = next((k for k in STORED_KITABS if k.id == kitab_id), None)
        if not found:
            return success_response(data=None, message="Kitab tidak ditemukan", status_code=404)
        return success_response(data=found.dict(), message="Detail kitab ditemukan")

kitab_controller = KitabController()
