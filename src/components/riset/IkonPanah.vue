<!-- Panah ▸ yang berputar ke bawah ▾ saat grup dibuka -->
<script setup>
defineProps({
  terbuka: { type: Boolean, default: false },
})
</script>

<template>
  <svg
    aria-hidden="true"
    class="h-4 w-4 shrink-0 text-hijau transition-transform duration-150"
    :class="terbuka ? 'rotate-90' : ''"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    stroke-width="2.4"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path d="M9 6l6 6-6 6" />
  </svg>
</template>
