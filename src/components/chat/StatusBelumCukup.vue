<!-- Kartu kuning "LAPORAN RISET BELUM CUKUP · Kesimpulan ditahan" -->
<script setup>
import { useSesiChat } from '../../composables/useSesiChat'
import { useRiset } from '../../composables/useRiset'
import { laporanBelumCukup } from '../../data/dataJawaban'
import KartuStatus from '../umum/KartuStatus.vue'
import DaftarLangkah from '../umum/DaftarLangkah.vue'
import TombolAksi from '../umum/TombolAksi.vue'

const { cobaLagi, ubahPertanyaan } = useSesiChat()
const { bukaModal } = useRiset()
</script>

<template>
  <KartuStatus
    nada="kuning"
    ikon="segitiga"
    :label="laporanBelumCukup.label"
    :judul="laporanBelumCukup.judul"
    :deskripsi="laporanBelumCukup.deskripsi"
  >
    <DaftarLangkah :items="laporanBelumCukup.rincian" />

    <template #aksi>
      <TombolAksi varian="utama" @click="bukaModal">Ubah sumber</TombolAksi>
      <TombolAksi @click="ubahPertanyaan">Ubah pertanyaan</TombolAksi>
      <TombolAksi @click="cobaLagi">Risetkan ulang gratis</TombolAksi>
    </template>
  </KartuStatus>
</template>
