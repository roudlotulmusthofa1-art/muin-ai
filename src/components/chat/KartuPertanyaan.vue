<!-- Kartu "PERTANYAAN ANDA" dengan garis biru tua di kiri -->
<script setup>
import { computed } from 'vue'
import { useSesiChat } from '../../composables/useSesiChat'
import { useRiset } from '../../composables/useRiset'

const { pertanyaanAktif, ringkasCakupan } = useSesiChat()
const { risetAktif } = useRiset()

const labelMode = {
  otomatis: 'Sumber otomatis',
  'pilih-sumber': 'Fokus sumber pilihan',
  'satu-kitab': 'Studi satu kitab',
  'semua-kitab': 'Semua kitab',
}

// Label kecil di bawah pertanyaan
const daftarTag = computed(() => [
  ringkasCakupan.value.bidang,
  ringkasCakupan.value.tugas,
  labelMode[risetAktif.value.mode],
  'Data demo',
])
</script>

<template>
  <section class="rounded-2xl border border-l-4 border-garis border-l-navy bg-kertas px-6 py-5">
    <p class="text-[11px] font-bold tracking-[0.14em] text-hijau uppercase">Pertanyaan Anda</p>
    <h2 class="mt-2 text-xl leading-snug font-bold text-navy">{{ pertanyaanAktif.teks }}</h2>
    <ul class="mt-2 flex flex-wrap gap-x-4 gap-y-1 text-[11px] text-ink-soft">
      <li v-for="tag in daftarTag" :key="tag">{{ tag }}</li>
    </ul>
  </section>
</template>
