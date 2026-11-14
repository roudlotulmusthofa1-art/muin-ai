<!--
  Halaman "Akun" (alamat: /akun).
  Kartu-kartunya dibuat otomatis dari data/dataAkun.js dengan v-for,
  jadi menambah kartu baru cukup menambah data, tanpa mengubah file ini.
-->
<script setup>
import { ref } from 'vue'
import { bagianAkun } from '../data/dataAkun'
import TataLetakHalaman from '../components/umum/TataLetakHalaman.vue'
import KartuBagian from '../components/umum/KartuBagian.vue'
import TombolAksi from '../components/umum/TombolAksi.vue'
import BarisInfo from '../components/akun/BarisInfo.vue'

// Prototipe: tombol keluar hanya menampilkan pesan
const pesanKeluar = ref('')
function keluar() {
  pesanKeluar.value = 'Simulasi: di aplikasi sungguhan, Anda akan keluar dari perangkat ini.'
}
</script>

<template>
  <TataLetakHalaman
    judul="Akun"
    subjudul="Langganan, keamanan, dan privasi"
    label="Akun"
    judul-besar="Satu halaman, tanpa labirin pengaturan"
    deskripsi="Informasi penting disusun vertikal dari akses ilmiah hingga privasi."
  >
    <div class="space-y-3">
      <KartuBagian
        v-for="bagian in bagianAkun"
        :key="bagian.judul"
        :judul="bagian.judul"
        :deskripsi="bagian.deskripsi"
      >
        <BarisInfo v-for="b in bagian.baris" :key="b.label" :label="b.label" :nilai="b.nilai" />
      </KartuBagian>

      <!-- Kartu bergaris merah untuk aksi penting -->
      <KartuBagian
        judul="Keluar"
        deskripsi="Keluar dari perangkat ini. Riwayat tetap mengikuti aturan hapus otomatis."
        nada="bahaya"
      >
        <TombolAksi varian="bahaya" @click="keluar">Keluar dari akun demo</TombolAksi>
        <p v-if="pesanKeluar" class="mt-3 text-xs text-ink-soft" aria-live="polite">
          {{ pesanKeluar }}
        </p>
      </KartuBagian>
    </div>
  </TataLetakHalaman>
</template>
