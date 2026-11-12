<!--
  Halaman sementara untuk menu yang belum dibuat (Riwayat, Ekspor, Akun).
  Judulnya diambil dari "meta.judul" di router/index.js, jadi satu file ini
  bisa dipakai untuk banyak alamat sekaligus.
-->
<script setup>
import { useRoute, RouterLink } from 'vue-router'
import TombolMenu from '../components/umum/TombolMenu.vue'

// useRoute() = info alamat yang sedang dibuka (nama, path, meta, dll.)
const route = useRoute()
</script>

<template>
  <div class="flex h-full flex-col bg-[#F7F2E8]">


    <div class="flex min-h-0 flex-1">


      <main class="relative flex flex-1 flex-col items-center justify-center px-6 text-center">
        <TombolMenu class="absolute top-4 left-4" />
        <p class="text-[11px] font-semibold tracking-wider text-ink-faint uppercase">
          Segera hadir
        </p>
        <h1 class="mt-2 text-2xl font-bold text-navy">{{ route.meta.judul }}</h1>
        <p class="mt-2 max-w-sm text-sm text-ink-soft">
          Halaman ini belum dibuat di prototipe. Alamatnya sudah ada di router, tinggal diisi nanti.
        </p>
        <RouterLink
          :to="{ name: 'beranda' }"
          class="mt-6 rounded-xl border border-garis bg-kertas px-4 py-2.5 text-sm font-bold text-navy transition hover:bg-white"
        >
          Kembali ke beranda
        </RouterLink>
      </main>
    </div>
  </div>
</template>
