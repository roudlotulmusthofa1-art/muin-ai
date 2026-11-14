<!--
  Halaman "Ekspor" (alamat: /ekspor). Tiga langkah:
  1. Pilih hasil   → PilihHasil.vue
  2. Pilih format  → PilihFormat.vue
  3. Buat ekspor   → tombol, logikanya ada di composables/useEkspor.js
-->
<script setup>
import { useEkspor } from '../composables/useEkspor'
import TataLetakHalaman from '../components/umum/TataLetakHalaman.vue'
import KartuBagian from '../components/umum/KartuBagian.vue'
import TombolAksi from '../components/umum/TombolAksi.vue'
import PilihHasil from '../components/ekspor/PilihHasil.vue'
import PilihFormat from '../components/ekspor/PilihFormat.vue'

const { pilihanHasil, hasilDipilih, format, pesan, bisaBuat, buatEkspor } = useEkspor()
</script>

<template>
  <TataLetakHalaman
    judul="Ekspor"
    subjudul="Buat berkas dari hasil yang masih hidup"
    label="Ekspor"
    judul-besar="Buat salinan sebelum hasil terhapus"
    deskripsi="Muin membuat berkas sesuai permintaan dan tidak menyimpannya sebagai arsip permanen."
  >
    <div class="space-y-3">
      <KartuBagian judul="1. Pilih hasil">
        <PilihHasil v-model="hasilDipilih" :pilihan="pilihanHasil" />
      </KartuBagian>

      <KartuBagian judul="2. Pilih format">
        <PilihFormat v-model="format" />
        <p class="mt-3 text-xs text-ink-soft">
          Ekspor memuat label AI, status hasil, pertanyaan, ibarah, sitasi, keterbatasan, dan versi
          sumber demonstrasi.
        </p>
      </KartuBagian>

      <KartuBagian
        judul="3. Pratinjau dan buat"
        deskripsi="Berkas server sementara dihapus maksimal 24 jam setelah permintaan."
      >
        <TombolAksi varian="utama" :disabled="!bisaBuat" @click="buatEkspor">
          Buat ekspor demo
        </TombolAksi>
        <p v-if="!bisaBuat" class="mt-2 text-xs text-[#a23a3a]">Pilih minimal satu hasil.</p>
        <!-- aria-live: pembaca layar ikut membacakan pesan ini saat muncul -->
        <p v-if="pesan" class="mt-3 text-xs font-semibold text-hijau" aria-live="polite">
          {{ pesan }}
        </p>
      </KartuBagian>
    </div>
  </TataLetakHalaman>
</template>
