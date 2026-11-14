<!-- Bagian atas halaman chat: judul + label status + tombol ukuran teks -->
<script setup>
import { useSesiChat } from '../../composables/useSesiChat'
import LencanaPil from '../umum/LencanaPil.vue'
import KepalaHalaman from '../umum/KepalaHalaman.vue'

const { sedangBerjalan } = useSesiChat()
</script>

<template>
  <!-- Memakai KepalaHalaman (sama dengan halaman lain), ditambah satu lencana khusus chat -->
  <KepalaHalaman judul="Chat" subjudul="Meja Baca Tenang">
    <span class="hidden md:block">
      <LencanaPil>
        {{ sedangBerjalan ? 'Pekerjaan aktif · hingga 7 hari' : 'Terhapus dalam 2 hari 18 jam' }}
      </LencanaPil>
    </span>
  </KepalaHalaman>
</template>
