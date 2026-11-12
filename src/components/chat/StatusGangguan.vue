<!-- Kartu merah "GANGGUAN TEKNIS · Pekerjaan belum dapat diselesaikan" -->
<script setup>
import { useSesiChat } from '../../composables/useSesiChat'
import { laporanGangguan } from '../../data/dataJawaban'
import KartuStatus from '../umum/KartuStatus.vue'
import TombolAksi from '../umum/TombolAksi.vue'

const { cobaLagi, ubahPertanyaan } = useSesiChat()
</script>

<template>
  <KartuStatus
    nada="merah"
    ikon="seru"
    :label="laporanGangguan.label"
    :judul="laporanGangguan.judul"
    :deskripsi="laporanGangguan.deskripsi"
  >
    <template #catatan>
      <p class="text-[11px] text-ink-soft">
        Kode bantuan: {{ laporanGangguan.kodeBantuan }} · tidak memuat isi pertanyaan
      </p>
    </template>

    <template #aksi>
      <TombolAksi varian="utama" @click="cobaLagi">Coba lagi gratis</TombolAksi>
      <TombolAksi @click="ubahPertanyaan">Ubah pertanyaan</TombolAksi>
    </template>
  </KartuStatus>
</template>
