<script setup>
import TombolMenu from './umum/TombolMenu.vue'

const emit = defineEmits(['buka-riwayat', 'ganti-bahasa', 'buka-profil'])



defineProps({
  labelRiwayat: { type: String, default: 'Riwayat 3 Hari' },
  bahasa: { type: String, default: 'ID' },
})
</script>

<template>
  <header class="flex items-center justify-between px-6 py-6 md:px-16">

    <!-- HAMBURGER: komponen yang sama dengan halaman lain (hilang saat menu terbuka) -->
    <TombolMenu />

    <nav class="ml-auto flex items-center gap-8 text-sm font-semibold text-ink">
      <!-- RIWAYAT -->
      <button type="button" class="transition hover:text-[#1e5e38]" @click="emit('buka-riwayat')">
        {{ labelRiwayat }}
      </button>

      <!-- BAHASA -->
      <button type="button" class="flex items-center gap-2 transition hover:text-[#1e5e38]" @click="emit('ganti-bahasa')">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">
          <circle cx="12" cy="12" r="9" />
          <path d="M3 12h18M12 3c2.8 3 2.8 15 0 18M12 3c-2.8 3-2.8 15 0 18" />
        </svg>
        <span>{{ bahasa }}</span>
      </button>

      <!-- PROFIL -->
      <button type="button" class="transition hover:text-[#1e5e38]" aria-label="Profil" @click="emit('buka-profil')">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round">
          <circle cx="12" cy="8" r="4" />
          <path d="M4 21c0-4 3.6-6.5 8-6.5s8 2.5 8 6.5" />
        </svg>
      </button>
    </nav>
  </header>
</template>
