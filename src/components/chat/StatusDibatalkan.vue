<!-- Kartu setelah pengguna menekan "Batalkan" -->
<script setup>
import { useSesiChat } from '../../composables/useSesiChat'
import { laporanDibatalkan } from '../../data/dataJawaban'
import KartuStatus from '../umum/KartuStatus.vue'
import TombolAksi from '../umum/TombolAksi.vue'

const { cobaLagi, ubahPertanyaan } = useSesiChat()
</script>

<template>
  <KartuStatus
    nada="netral"
    ikon="seru"
    :label="laporanDibatalkan.label"
    :judul="laporanDibatalkan.judul"
    :deskripsi="laporanDibatalkan.deskripsi"
  >
    <template #aksi>
      <TombolAksi varian="utama" @click="cobaLagi">Mulai lagi</TombolAksi>
      <TombolAksi @click="ubahPertanyaan">Ubah pertanyaan</TombolAksi>
    </template>
  </KartuStatus>
</template>
