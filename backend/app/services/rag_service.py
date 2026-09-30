import logging
from typing import List, Dict, Any, Optional
from rank_bm25 import BM25Okapi

from ..config import settings
from ..models import ChatRequest, ChatResponse, Citation, KitabChunk
from ..helpers import normalize_arabic, remove_tashkeel, format_citation
from .router_service import router_service
from .vector_service import vector_service

logger = logging.getLogger(__name__)

class RAGService:
    """Core RAG Service: Hybrid Retrieval (Dense Vector + BM25) & Grounding Prompt Builder"""

    def __init__(self):
        self._bm25_corpus: List[KitabChunk] = []
        self._bm25_index: Optional[BM25Okapi] = None
        self._seed_sample_kitab_data()

    def _seed_sample_kitab_data(self):
        """Memuat data kutipan kitab turats awal sebagai acuan ilmiah demo & testing"""
        sample_chunks = [
            KitabChunk(
                chunk_id="fathul-qarib_wudhu_1",
                kitab_id="fathul-qarib",
                kitab_name="Fathul Qarib Al-Mujib",
                muallif="Ibnu Qasim Al-Ghazi",
                wafat_year=918,
                bidang="Fikih",
                mazhab="Syafi'i",
                kategori_sumber="mutun",
                juz=1,
                halaman=14,
                bab="Kitab At-Thaharah",
                fasl="Fasl Furudh Al-Wudhu",
                text_arabic="وفروض الوضوء ستة أشياء: الأول النية عند غسل الوجه، والثاني غسل الوجه، والثالث غسل اليدين مع المرفقين، والرابع مسح بعض الرأس، والخامس غسل الرجلين مع الكعبين، والسادس الترتيب.",
                text_clean=normalize_arabic("وفروض الوضوء ستة أشياء: الأول النية عند غسل الوجه، والثاني غسل الوجه، والثالث غسل اليدين مع المرفقين، والرابع مسح بعض الرأس، والخامس غسل الرجلين مع الكعبين، والسادس الترتيب.")
            ),
            KitabChunk(
                chunk_id="fathul-muin_shalah_1",
                kitab_id="fathul-muin",
                kitab_name="Fathul Mu'in bi Syarh Qurratil 'Ain",
                muallif="Zainuddin Al-Malibari",
                wafat_year=987,
                bidang="Fikih",
                mazhab="Syafi'i",
                kategori_sumber="mutun",
                juz=1,
                halaman=32,
                bab="Bab As-Shalah",
                fasl="Syurut As-Shalah",
                text_arabic="وشروط الصلاة خمسة: طهارة الحدثين، وطهارة النجس في الثوب والبدن والمكان، وستر العورة، واستقبال القبلة، ودخول الوقت.",
                text_clean=normalize_arabic("وشروط الصلاة خمسة: طهارة الحدثين، وطهارة النجس في الثوب والبدن والمكان، وستر العورة، واستقبال القبلة، ودخول الوقت.")
            ),
            KitabChunk(
                chunk_id="safinah_shalah_1",
                kitab_id="safinatun-naja",
                kitab_name="Safinatun Naja",
                muallif="Salim bin Sumair Al-Hadhrami",
                wafat_year=1271,
                bidang="Fikih",
                mazhab="Syafi'i",
                kategori_sumber="mutun",
                juz=1,
                halaman=8,
                bab="Bab As-Shalah",
                fasl="Arkan As-Shalah",
                text_arabic="أركان الصلاة سبعة عشر: الأول النية، الثاني تكبيرة الإحرام، الثالث القيام مع القدرة في الفرض، الرابع قراءة الفاتحة...",
                text_clean=normalize_arabic("أركان الصلاة سبعة عشر: الأول النية، الثاني تكبيرة الإحرام، الثالث القيام مع القدرة في الفرض، الرابع قراءة الفاتحة...")
            ),
            KitabChunk(
                chunk_id="ibn_katsir_alfatihah_1",
                kitab_id="tafsir-ibn-katsir",
                kitab_name="Tafsir Al-Qur'an Al-'Azhim",
                muallif="Ibnu Katsir Ad-Dimasyqi",
                wafat_year=774,
                bidang="Tafsir",
                mazhab="Jumhur",
                kategori_sumber="mutun",
                juz=1,
                halaman=102,
                bab="Surat Al-Fatihah",
                fasl="Tafsir Basmalah",
                text_arabic="افتتح بها الصحابة كتاب الله، وأجمع العلماء على أنها بعض آية من سورة النمل، ثم اختلفوا: هل هي آية مستقلة في أول كل سورة، أو من أول كل سورة كالفاتحة...",
                text_clean=normalize_arabic("افتتح بها الصحابة كتاب الله، وأجمع العلماء على أنها بعض آية من سورة النمل، ثم اختلفوا: هل هي آية مستقلة في أول كل سورة، أو من أول كل سورة كالفاتحة...")
            )
        ]
        self.add_chunks_to_corpus(sample_chunks)

    def add_chunks_to_corpus(self, chunks: List[KitabChunk]):
        """Menambahkan chunk baru ke dalam corpus BM25 in-memory"""
        self._bm25_corpus.extend(chunks)
        tokenized_corpus = [ch.text_clean.split() for ch in self._bm25_corpus]
        self._bm25_index = BM25Okapi(tokenized_corpus)

    def _bm25_search(self, query: str, limit: int = 5, kitab_ids: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Pencarian leksikal persis dengan BM25 atas teks Arab bersih"""
        if not self._bm25_index or not self._bm25_corpus:
            return []

        clean_query = normalize_arabic(query)
        tokenized_query = clean_query.split()
        if not tokenized_query:
            return []

        scores = self._bm25_index.get_scores(tokenized_query)
        ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

        results = []
        for idx, score in ranked:
            if score <= 0:
                continue
            chunk = self._bm25_corpus[idx]
            if kitab_ids and chunk.kitab_id not in kitab_ids:
                continue
            results.append({
                "score": float(score),
                "payload": chunk.dict()
            })
            if len(results) >= limit:
                break
        return results

    async def retrieve_context(
        self,
        query: str,
        scope: str,
        kitab_ids: Optional[List[str]] = None,
        limit: int = 4
    ) -> List[Dict[str, Any]]:
        """Hybrid Search: Menggabungkan hasil BM25 dan Dense Vector Qdrant"""
        # 1. BM25 Search
        bm25_res = self._bm25_search(query, limit=limit, kitab_ids=kitab_ids)

        # 2. Vector Search
        try:
            vector_res = await vector_service.search(query, limit=limit, kitab_ids=kitab_ids)
        except Exception as e:
            logger.warning("Vector search error (%s), fallback ke BM25 saja.", e)
            vector_res = []

        # 3. Simple Reciprocal Rank Fusion (RRF)
        scores_map: Dict[str, Dict[str, Any]] = {}
        for rank, item in enumerate(bm25_res):
            cid = item["payload"]["chunk_id"]
            rrf = 1.0 / (60 + rank + 1)
            scores_map[cid] = {"score": rrf, "payload": item["payload"]}

        for rank, item in enumerate(vector_res):
            cid = item["payload"]["chunk_id"]
            rrf = 1.0 / (60 + rank + 1)
            if cid in scores_map:
                scores_map[cid]["score"] += rrf
            else:
                scores_map[cid] = {"score": rrf, "payload": item["payload"]}

        # Urutkan berdasarkan skor fusi tertinggi
        merged = sorted(scores_map.values(), key=lambda x: x["score"], reverse=True)
        return merged[:limit]

    def _build_system_prompt(self, scope: str, only_selected: bool) -> str:
        prompt = (
            "Anda adalah Muin AI, asisten riset ilmiah Islam spesialisasi Fikih (terutama Mazhab Syafi'i), "
            "Ushul Fikih, dan Tafsir Al-Qur'an. Tugas Anda adalah memberikan jawaban riset yang akurat, "
            "bermartabat, dan bersumber secara ketat dari teks kitab turats (kitab kuning) yang diberikan dalam konteks rujukan.\n\n"
            "Pedoman Riset:\n"
            "1. SETIAP kesimpulan hukum, tafsir, atau penjelasan WAJIB menyertakan Ibarah Arab asli dari teks sumber.\n"
            "2. Berikan terjemahan dan penjelasan (syarah) bahasa Indonesia yang jernih, runtut, dan mudah dipahami.\n"
            "3. Cantumkan sitasi lengkap di akhir penjelasan dengan format: Nama Kitab, Mu'allif, Tahun Wafat (bila ada), Juz, dan Halaman.\n"
        )
        if only_selected:
            prompt += (
                "4. ATURAN KETAT: Pengguna mengaktifkan 'Hanya sumber yang saya pilih'. "
                "Jika konteks teks kitab di bawah ini tidak memuat jawaban atau tidak mencukupi, "
                "Anda DILARANG berhalusinasi atau mereka-reka hukum. Katakan dengan jujur dan santun bahwa "
                "sumber terpilih belum memuat pembahasan tersebut, lalu tahan kesimpulan.\n"
            )
        else:
            prompt += (
                "4. Utamakan teks rujukan terlampir. Jika ada konteks pendukung dasar dari kaidah umum mazhab, "
                "beri label secara terpisah sebagai catatan pelengkap.\n"
            )

        if scope == "fikih-syafii-ibarah":
            prompt += "\nMode Khusus: Jelaskan struktur kalimat Arab (i'rab/makna ibarah), maksud ulama pengarang, dan kedudukan hukumnya."
        elif scope == "tafsir":
            prompt += "\nMode Khusus: Paparkan sababun nuzul, munasabah, dan penafsiran ulama salaf/khalaf berdasarkan kitab tafsir mu'tabar."

        return prompt

    async def answer_question(self, req: ChatRequest) -> ChatResponse:
        """Memproses pertanyaan pengguna dengan hybrid retrieval dan 9Router gateway"""
        # 1. Retrieve relevansi dari kitab
        contexts = await self.retrieve_context(
            query=req.question,
            scope=req.scope,
            kitab_ids=req.selected_kitab_ids
        )

        # 2. Susun kutipan dan sitasi
        citations: List[Citation] = []
        context_text = ""

        for idx, item in enumerate(contexts):
            p = item["payload"]
            cit = Citation(
                kitab_id=p["kitab_id"],
                kitab_name=p["kitab_name"],
                muallif=p["muallif"],
                wafat_year=p.get("wafat_year"),
                juz=p.get("juz", 1),
                halaman=p.get("halaman", 1),
                bab=p.get("bab"),
                fasl=p.get("fasl"),
                ibarah_arab=p["text_arabic"],
                relevance_score=round(item["score"] * 100, 2)
            )
            citations.append(cit)
            context_text += (
                f"\n--- [Rujukan {idx+1}] ---\n"
                f"Kitab: {p['kitab_name']} (Karya: {p['muallif']}, w. {p.get('wafat_year', '-')} H)\n"
                f"Juz/Hal: Juz {p.get('juz', 1)}, Hal {p.get('halaman', 1)}\n"
                f"Ibarah Arab:\n{p['text_arabic']}\n"
            )

        # 3. Rakit pesan untuk 9Router
        system_prompt = self._build_system_prompt(req.scope, req.only_selected_sources)
        user_message = (
            f"Pertanyaan Pengguna: {req.question}\n\n"
            f"Konteks Teks Kitab yang Tersedia:\n{context_text if context_text else '(Tidak ditemukan teks yang cocok dalam database)'}\n\n"
            "Berikan jawaban terstruktur lengkap dengan Ibarah Arab dan sitasi yang dapat diperiksa."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]

        # 4. Panggil 9Router AI Gateway
        try:
            ai_result = await router_service.chat_completion(messages=messages)
            answer_content = ai_result["content"]
            model_used = ai_result["model_used"]
        except Exception as e:
            logger.error("Error dari 9Router: %s", e)
            # Jika 9Router belum running lokal, berikan respon deterministik cerdas berbasis ibarah yang terambil
            if citations:
                primary = citations[0]
                answer_content = (
                    f"Berdasarkan penelusuran kitab **{primary.kitab_name}**, berikut penjelasan atas pertanyaan Anda:\n\n"
                    f"**Ibarah Teks:**\n> {primary.ibarah_arab}\n\n"
                    f"**Penjelasan:**\nMasalah tersebut telah dijelaskan oleh {primary.muallif} dalam bab {primary.bab or 'terkait'}. "
                    f"Rujukan dapat diperiksa langsung pada {format_citation(primary.kitab_name, primary.muallif, primary.wafat_year, primary.juz, primary.halaman)}."
                )
                model_used = "muin-offline-engine"
            else:
                answer_content = (
                    "Mohon maaf, belum ditemukan ibarah kitab yang mencukupi untuk menjawab masalah ini pada sumber yang dipilih. "
                    "Silakan periksa pilihan kitab pada panel sumber atau perluas cakupan pencarian."
                )
                model_used = "muin-offline-engine"

        primary_ibarah = citations[0].ibarah_arab if citations else None

        return ChatResponse(
            question=req.question,
            scope=req.scope,
            source=req.source,
            answer=answer_content,
            ibarah=primary_ibarah,
            citations=citations,
            model_used=model_used
        )

rag_service = RAGService()
