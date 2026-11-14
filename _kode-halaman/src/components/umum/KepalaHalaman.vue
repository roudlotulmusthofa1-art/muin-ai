<!--
  Bagian atas setiap halaman (Chat, Riwayat, Ekspor, Akun):
  [☰] Judul + subjudul ............ [lencana tambahan] [Data demonstrasi] [Aa]

  Props : judul, subjudul
  Slot  : lencana tambahan di kanan (opsional), contoh "Pekerjaan aktif" di halaman chat
-->
<script setup>
import { useSesiChat } from '../../composables/useSesiChat'
import LencanaPil from './LencanaPil.vue'
import TombolMenu from './TombolMenu.vue'

defineProps({
  judul: { type: String, required: true },
  subjudul: { type: String, default: '' },
})

const { teksBesar, gantiUkuranTeks } = useSesiChat()
</script>

<template>
  <header class="flex items-center justify-between gap-4 border-b border-black/10 px-5 py-4 lg:px-11">
    <div class="flex items-center gap-3">
      <!-- Tombol ☰: buka / tutup menu samping -->
      <TombolMenu />
      <div>
        <h1 class="text-[17px] font-bold text-navy">{{ judul }}</h1>
        <p v-if="subjudul" class="text-xs text-ink-soft">{{ subjudul }}</p>
      </div>
    </div>

    <div class="flex items-center gap-2">
      <!-- Lencana tambahan dari halaman yang memakai komponen ini -->
      <slot />

      <!-- Dibungkus <span> supaya "hidden" tidak bertabrakan dengan "inline-flex" milik LencanaPil -->
      <span class="hidden sm:block">
        <LencanaPil titik>Data demonstrasi</LencanaPil>
      </span>
      <button
        type="button"
        class="flex h-10 w-10 items-center justify-center rounded-xl border border-garis text-[15px] text-navy transition hover:bg-white"
        :class="teksBesar ? 'bg-hijau-muda' : 'bg-kertas'"
        :aria-pressed="teksBesar"
        aria-label="Perbesar teks jawaban"
        @click="gantiUkuranTeks"
      >
        Aa
      </button>
    </div>
  </header>
</template>
