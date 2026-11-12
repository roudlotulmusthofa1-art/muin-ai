<!--
  KHUSUS PROTOTIPE: tombol kecil di kiri bawah untuk memilih hasil akhir riset,
  supaya semua tampilan (selesai / belum cukup / gangguan) bisa dicoba.
  Hapus komponen ini kalau sudah tersambung ke backend sungguhan.
-->
<script setup>
import { useSesiChat } from '../../composables/useSesiChat'

const { skenarioDemo, pilihSkenario } = useSesiChat()

const daftarSkenario = [
  { id: 'selesai', label: 'Selesai' },
  { id: 'belum-cukup', label: 'Belum cukup' },
  { id: 'gangguan', label: 'Gangguan' },
]
</script>

<template>
  <div
    class="fixed bottom-3 left-3 z-30 hidden items-center gap-1 rounded-full border border-black/10 bg-white/85 p-1 text-[10px] font-semibold tracking-wider text-ink-soft uppercase backdrop-blur md:flex"
    role="group"
    aria-label="Pilih hasil demo"
  >
    <span class="px-2">Demo hasil</span>
    <button
      v-for="s in daftarSkenario"
      :key="s.id"
      type="button"
      class="rounded-full px-2.5 py-1 transition"
      :class="skenarioDemo === s.id ? 'bg-navy text-white' : 'hover:bg-black/5'"
      :aria-pressed="skenarioDemo === s.id"
      @click="pilihSkenario(s.id)"
    >
      {{ s.label }}
    </button>
  </div>
</template>
