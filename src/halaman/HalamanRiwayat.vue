<!--
  Halaman "Riwayat 3 Hari" (alamat: /riwayat).
  Klik salah satu kartu → hasil itu dibuka lagi di halaman chat.
-->
<script setup>
import { dataRiwayat } from '../data/dataRiwayat'
import { useSesiChat } from '../composables/useSesiChat'
import TataLetakHalaman from '../components/umum/TataLetakHalaman.vue'
import KartuRiwayat from '../components/riwayat/KartuRiwayat.vue'

const { bukaRiwayat } = useSesiChat()
</script>

<template>
  <TataLetakHalaman
    judul="Riwayat 3 Hari"
    subjudul="Terbaru dan akan terhapus otomatis"
    label="Riwayat 3 Hari"
    judul-besar="Hasil yang masih hidup"
    deskripsi="Riwayat disusun terbaru lebih dahulu. Ekspor hasil penting sebelum waktu habis."
  >
    <div class="space-y-3">
      <KartuRiwayat v-for="item in dataRiwayat" :key="item.id" :item="item" @pilih="bukaRiwayat" />
    </div>
  </TataLetakHalaman>
</template>
