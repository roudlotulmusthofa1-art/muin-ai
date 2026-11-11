<!-- Isi tab "Kitab": kolom cari + daftar kitab -->
<script setup>
import { ref, computed } from 'vue'
import { dataKitab } from '../../data/dataKitab'
import { namaMuallif } from '../../data/dataMuallif'
import GrupKitab from './GrupKitab.vue'

const kataKunci = ref('')

const kitabCocok = computed(() => {
  const cari = kataKunci.value.trim().toLowerCase()
  if (!cari) return dataKitab
  return dataKitab.filter(
    (k) => k.judul.toLowerCase().includes(cari) || namaMuallif(k.muallifId).toLowerCase().includes(cari),
  )
})
</script>

<template>
  <div class="space-y-3">
    <input
      v-model="kataKunci"
      type="search"
      placeholder="Cari kitab atau mu’allif..."
      class="h-11 w-full rounded-xl border border-garis bg-white px-3 text-sm text-ink placeholder:text-ink-faint focus:border-hijau focus:outline-none"
    />

    <!-- Saat mencari, grup otomatis terbuka supaya hasil langsung terlihat -->
    <GrupKitab
      judul="Daftar kitab Fikih · Syafi’i"
      keterangan="Klik untuk membuka atau meringkas tanpa mengubah pilihan"
      :label-jumlah="`${kitabCocok.length} kitab`"
      :kitab="kitabCocok"
      :pakai-centang="false"
      :paksa-buka="kataKunci.trim() !== ''"
    />
  </div>
</template>
