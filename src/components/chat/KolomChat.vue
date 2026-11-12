<!--
  Kolom tanya lanjutan di bawah halaman chat.
  "sticky bottom-0" membuatnya menempel di bawah layar saat isi halaman panjang.
  dir="auto" membuat arah teks otomatis: Arab → kanan ke kiri, Latin → kiri ke kanan.
-->
<script setup>
import { ref, computed, watch } from 'vue'
import { useSesiChat } from '../../composables/useSesiChat'

const { teksLanjutan, sedangBerjalan, kirimLanjutan } = useSesiChat()

const kolom = ref(null)

const bisaKirim = computed(() => teksLanjutan.value.trim().length > 0 && !sedangBerjalan.value)

const placeholder = computed(() =>
  sedangBerjalan.value
    ? 'Tunggu sampai pekerjaan selesai atau batalkan riset.'
    : 'Tanyakan lanjutan tentang masalah yang sama...',
)

// Tinggi kolom ikut bertambah sesuai isi (maksimal 180px)
function aturTinggi() {
  const el = kolom.value
  if (!el) return
  el.style.height = 'auto'
  el.style.height = `${Math.min(el.scrollHeight, 180)}px`
}
// Dijalankan juga saat isi diubah dari luar (contoh: tombol "Ubah pertanyaan")
watch(teksLanjutan, () => requestAnimationFrame(aturTinggi))

// Enter = kirim, Shift+Enter = baris baru
function tekanTombol(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    kirimLanjutan()
  }
}
</script>

<template>
  <div class="sticky bottom-0 bg-linear-to-t from-[#F7F2E8] from-70% to-transparent pt-6 pb-5">
    <form
      class="flex items-end gap-3 rounded-2xl border border-garis bg-kertas py-2.5 pr-2.5 pl-5 shadow-input"
      @submit.prevent="kirimLanjutan"
    >
      <label for="kolom-chat" class="sr-only">Pertanyaan lanjutan</label>
      <textarea
        id="kolom-chat"
        ref="kolom"
        v-model="teksLanjutan"
        rows="1"
        dir="auto"
        :disabled="sedangBerjalan"
        :placeholder="placeholder"
        class="flex-1 resize-none bg-transparent py-2.5 text-[15px] leading-6 text-ink placeholder:text-ink-soft/80 focus:outline-none disabled:cursor-not-allowed"
        @keydown="tekanTombol"
      />
      <button
        type="submit"
        :disabled="!bisaKirim"
        class="flex shrink-0 items-center gap-1.5 rounded-xl bg-hijau px-4 py-3 text-[15px] font-bold text-white transition hover:bg-hijau-tua disabled:cursor-not-allowed disabled:bg-hijau/40"
      >
        <span aria-hidden="true">↑</span>
        Kirim
      </button>
    </form>

    <p class="mt-3 flex flex-wrap justify-center gap-x-4 text-[11px] text-ink-soft">
      <strong class="text-xs font-bold text-navy">Arah teks: Otomatis</strong>
      <span class="hidden sm:inline">· Desktop: Enter kirim, Shift+Enter baris baru</span>
    </p>
  </div>
</template>
