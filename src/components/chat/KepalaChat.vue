<!-- Bagian atas halaman chat: judul + label status + tombol ukuran teks -->
<script setup>
import { useSesiChat } from '../../composables/useSesiChat'
import LencanaPil from '../umum/LencanaPil.vue'
import TombolMenu from '../umum/TombolMenu.vue'

const { sedangBerjalan, teksBesar, gantiUkuranTeks} = useSesiChat()
</script>

<template>
  <header class="flex items-center justify-between gap-4 border-b border-black/10 px-5 py-4 lg:px-11">
    <div class="flex items-center gap-3">
       <!-- Tombol ☰: buka / tutup menu samping -->
      <TombolMenu />
      <div>
        <h1 class="text-[17px] font-bold text-navy">Chat</h1>
        <p class="text-xs text-ink-soft">Meja Baca Tenang</p>
      </div>
    </div>

    <div class="flex items-center gap-2">
      <!--
        Dibungkus <span> karena LencanaPil sudah punya class "inline-flex".
        Kalau "hidden" ditaruh langsung di LencanaPil, dua class itu bertabrakan.
        hidden md:block = disembunyikan di layar kecil, tampil mulai layar sedang.
      -->
      <span class="hidden md:block">
        <LencanaPil>
          {{ sedangBerjalan ? 'Pekerjaan aktif · hingga 7 hari' : 'Terhapus dalam 2 hari 18 jam' }}
        </LencanaPil>
      </span>
      <span class="hidden sm:block">
        <LencanaPil titik>Data demonstrasi</LencanaPil>
      </span>
      <button
        type="button"
        class="flex h-10 w-10 items-center justify-center rounded-xl border border-garis text-[15px] text-navy transition hover:bg-white"
        :class="teksBesar ? 'bg-hijau-muda' : 'bg-kertas'"
        :aria-pressed="teksBesar"
        aria-label="Perbesar teks jawaban"
        @click="gantiUkuranTeks"
      >
        Aa
      </button>
    </div>
  </header>
</template>
