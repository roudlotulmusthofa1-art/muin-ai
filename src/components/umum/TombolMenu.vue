<!--
  Tombol ☰ (hamburger): membuka / menutup menu samping.
  Komponen kecil yang dipakai ulang di halaman chat dan halaman "Segera hadir".
-->
<script setup>
import { useMenuSamping } from '../../composables/useMenuSamping'

const { menuTerbuka, gantiMenu } = useMenuSamping()
</script>

<template>
  <button
    type="button"
    class="rounded-md p-1 text-ink transition hover:bg-black/5 hover:text-[#1e5e38]"
    :aria-label="menuTerbuka ? 'Tutup menu' : 'Buka menu'"
    :aria-expanded="menuTerbuka"
    @click="gantiMenu"
  >
    <svg
      width="22"
      height="22"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="1.8"
      stroke-linecap="round"
      aria-hidden="true"
    >
      <path d="M4 7h16M4 12h16M4 17h16" />
    </svg>
  </button>
</template>
