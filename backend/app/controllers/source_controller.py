from ..models import ResearchFieldGroup, KitabItem
from ..helpers import success_response

class SourceController:
    """Controller untuk mengelola daftar sumber dan fann dinamis pada ResearchSourcePanel.vue"""

    @staticmethod
    async def get_research_fields():
        fields = [
            ResearchFieldGroup(
                name="Fikih · Syafi'i",
                description="Urutan mu'allif berdasarkan tahun wafat",
                books="4 dari 6 kitab aktif",
                status="active",
                open=True,
                items=[
                    KitabItem(
                        id="safinatun-naja",
                        name="Safinatun Naja",
                        muallif="Salim bin Sumair Al-Hadhrami",
                        wafat_year=1271,
                        mazhab="Syafi'i",
                        bidang="Fikih",
                        total_pages=40
                    ),
                    KitabItem(
                        id="fathul-qarib",
                        name="Fathul Qarib Al-Mujib",
                        muallif="Ibnu Qasim Al-Ghazi",
                        wafat_year=918,
                        mazhab="Syafi'i",
                        bidang="Fikih",
                        total_pages=180
                    ),
                    KitabItem(
                        id="fathul-muin",
                        name="Fathul Mu'in bi Syarh Qurratil 'Ain",
                        muallif="Zainuddin Al-Malibari",
                        wafat_year=987,
                        mazhab="Syafi'i",
                        bidang="Fikih",
                        total_pages=320
                    ),
                    KitabItem(
                        id="minhaj-at-thalibin",
                        name="Minhajut Thalibin",
                        muallif="Imam An-Nawawi",
                        wafat_year=676,
                        mazhab="Syafi'i",
                        bidang="Fikih",
                        total_pages=450
                    )
                ]
            ),
            ResearchFieldGroup(
                name="Tafsir Al-Qur'an",
                description="Koleksi tafsir bil ma'tsur dan dirayah",
                books="2 kitab aktif",
                status="active",
                open=False,
                items=[
                    KitabItem(
                        id="tafsir-al-jalalain",
                        name="Tafsir Al-Jalalain",
                        muallif="Al-Mahalli & As-Suyuthi",
                        wafat_year=911,
                        mazhab="Syafi'i",
                        bidang="Tafsir",
                        total_pages=600
                    ),
                    KitabItem(
                        id="tafsir-ibn-katsir",
                        name="Tafsir Al-Qur'an Al-'Azhim",
                        muallif="Ibnu Katsir Ad-Dimasyqi",
                        wafat_year=774,
                        mazhab="Jumhur",
                        bidang="Tafsir",
                        total_pages=2400
                    )
                ]
            ),
            ResearchFieldGroup(
                name="Fikih · Hanafi",
                description="Bidang tidak aktif pada chat ini",
                books="5 kitab demo",
                status="inactive",
                open=False,
                items=[]
            ),
            ResearchFieldGroup(
                name="Usul Fikih",
                description="Domain terpisah",
                books="6 kitab demo",
                status="inactive",
                open=False,
                items=[]
            ),
            ResearchFieldGroup(
                name="Dua sumber tambahan",
                description="Belum lolos rilis demo",
                books="2 belum tersedia",
                status="warning",
                open=False,
                items=[]
            )
        ]

        return success_response(
            data=[f.dict() for f in fields],
            message="Kategori sumber riset berhasil dimuat"
        )

source_controller = SourceController()
