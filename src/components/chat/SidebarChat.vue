<!-- Menu samping kiri: logo, "Chat baru", menu, dan kartu konteks aktif. Disembunyikan di layar kecil. -->
<script setup>
import { useRoute, RouterLink } from 'vue-router'
import logo from '../../assets/logo.svg'
import { useSesiChat } from '../../composables/useSesiChat'
import { useMenuSamping } from '../../composables/useMenuSamping'
import KartuKonteksAktif from './KartuKonteksAktif.vue'

const { chatBaru } = useSesiChat()
const { tutupMenu } = useMenuSamping()

// id = nama route di src/router/index.js
// ikon = isi atribut "d" pada <path> SVG
const daftarMenu = [
  { id: 'chat', label: 'Chat', ikon: 'M4 5h16v11H9l-5 4z' },
  { id: 'riwayat', label: 'Riwayat 3 Hari', ikon: 'M3 12a9 9 0 1 0 2.6-6.4M3 4v4h4M12 8v4l3 2' },
  { id: 'ekspor', label: 'Ekspor', ikon: 'M12 4v11M7 10l5 5 5-5M5 20h14' },
  {
    id: 'akun',
    label: 'Akun',
    ikon: 'M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM4 21c0-4 3.6-6.5 8-6.5s8 2.5 8 6.5',
  },
]

// Menu yang menyala = menu yang namanya sama dengan nama route yang sedang dibuka
const route = useRoute()
</script>

<template>
  <!-- pb-14: ruang kosong di bawah untuk tombol "Demo hasil" (PilihSkenarioDemo) -->
  <aside
    class="relative flex h-full w-60 shrink-0 flex-col overflow-y-auto border-r border-black/5 bg-[#f5f0e5] px-4 pt-6 pb-14"
  >
    <!-- Tombol sembunyikan menu (pojok kanan atas) -->
    <button
      type="button"
      class="absolute top-3 right-3 flex h-8 w-8 items-center justify-center rounded-lg text-ink-soft transition hover:bg-black/5 hover:text-navy"
      aria-label="Sembunyikan menu"
      @click="tutupMenu"
    >
      <svg
        width="18"
        height="18"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="1.7"
        stroke-linecap="round"
        stroke-linejoin="round"
        aria-hidden="true"
      >
        <rect x="3" y="4" width="18" height="16" rx="2" />
        <path d="M9 4v16M15 10l-2 2 2 2" />
      </svg>
    </button>
    <!-- LOGO -->
    <div class="flex justify-center mt-5">
      <img :src="logo" alt="Muin AI" class="w-24" />
    </div>

    <!-- TOMBOL CHAT BARU -->
    <button
      type="button"
      class="mt-8 flex items-center justify-center gap-2 rounded-xl border border-garis bg-kertas py-3 text-[15px] font-bold text-navy transition hover:bg-white"
      @click="chatBaru"
    >
      <span class="text-hijau" aria-hidden="true">+</span>
      Chat baru
    </button>
    <nav class="mt-5 space-y-1.5" aria-label="Menu utama">
      <!-- RouterLink = pengganti <a href>, pindah halaman tanpa memuat ulang browser -->
      <RouterLink
        v-for="menu in daftarMenu"
        :key="menu.id"
        :to="{ name: menu.id }"
        class="flex w-full items-center gap-3 rounded-xl px-4 py-3 text-left text-[15px] transition"
        :class="
          menu.id === route.name
            ? 'border border-[#b9d8cf] bg-hijau-muda text-navy shadow-[inset_3px_0_0_var(--color-hijau)]'
            : 'border border-transparent text-ink-soft hover:bg-black/5'
        "
      >
        <svg
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="1.7"
          stroke-linecap="round"
          stroke-linejoin="round"
          aria-hidden="true"
        >
          <path :d="menu.ikon" />
        </svg>
        {{ menu.label }}
      </RouterLink>
    </nav>

    <!-- mt-auto mendorong kartu ini ke bagian paling bawah sidebar -->
    <KartuKonteksAktif class="mt-auto" />
  </aside>
</template>
