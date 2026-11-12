<!-- Kartu "PEKERJAAN AKTIF · Riset sedang berjalan" -->
<script setup>
import { computed } from 'vue'
import { useSesiChat } from '../../composables/useSesiChat'
import { LANGKAH_RISET } from '../../data/dataJawaban'
import KartuStatus from '../umum/KartuStatus.vue'
import DaftarLangkah from '../umum/DaftarLangkah.vue'
import TombolAksi from '../umum/TombolAksi.vue'

const { tahap, kitabDiperiksa, pertanyaanAktif, batalkan } = useSesiChat()

const deskripsi = computed(
  () =>
    `Memeriksa sumber yang Anda pilih. ${kitabDiperiksa.value} dari ${pertanyaanAktif.value.jumlahKitab} kitab demo telah diperiksa.`,
)

// Ubah daftar langkah menjadi item untuk DaftarLangkah:
// sebelum tahap = selesai, sama dengan tahap = berjalan, sesudah tahap = menunggu
const langkah = computed(() =>
  LANGKAH_RISET.map((item, i) => {
    if (i < tahap.value) return { status: 'selesai', teks: item.teks }
    if (i === tahap.value) return { status: 'berjalan', teks: item.teks }
    return { status: 'menunggu', teks: item.teksMenunggu ?? item.teks }
  }),
)
</script>

<template>
  <KartuStatus
    nada="netral"
    ikon="putar"
    label="Pekerjaan aktif"
    judul="Riset sedang berjalan"
    :deskripsi="deskripsi"
  >
    <DaftarLangkah :items="langkah" />

    <template #aksi>
      <TombolAksi varian="bahaya" @click="batalkan">Batalkan</TombolAksi>
    </template>
  </KartuStatus>
</template>
