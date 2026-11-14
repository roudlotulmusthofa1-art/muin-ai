<!--
  Satu kartu di halaman "Riwayat 3 Hari".
  Kiri  : judul + keterangan
  Kanan : sisa waktu (warnanya tergantung "nada")
  Saat diklik → mengirim sinyal "pilih" ke halaman yang memakainya.
-->
<script setup>
defineProps({
  item: { type: Object, required: true }, // satu baris dari dataRiwayat.js
})

const emit = defineEmits(['pilih'])

// Warna teks sisa waktu
const warnaSisa = {
  aman: 'text-hijau',
  segera: 'text-[#8a5a00]',
  aktif: 'text-hijau-tua',
}
</script>

<template>
  <button
    type="button"
    class="flex w-full items-center justify-between gap-4 rounded-2xl border border-garis bg-kertas px-5 py-5 text-left transition hover:border-[#c9bda9] hover:bg-white sm:px-6"
    @click="emit('pilih', item)"
  >
    <div class="min-w-0">
      <h3 class="text-[15px] font-bold text-navy">{{ item.judul }}</h3>
      <p class="mt-1.5 text-xs text-ink-soft">{{ item.keterangan }}</p>
    </div>
    <span class="shrink-0 text-xs font-bold" :class="warnaSisa[item.nada]">{{ item.sisa }}</span>
  </button>
</template>
