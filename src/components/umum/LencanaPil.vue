<!--
  Label bulat lonjong (pil). Contoh: "Data demonstrasi", "Terhapus dalam 2 hari 18 jam".
  titik = true → tampilkan titik hijau di depan teks.
-->
<script setup>
defineProps({
  titik: { type: Boolean, default: false },
})
</script>

<template>
  <span
    class="inline-flex items-center gap-2 rounded-full border border-garis bg-white px-3.5 py-2 text-xs font-semibold whitespace-nowrap text-navy"
  >
    <span v-if="titik" class="h-2 w-2 rounded-full bg-hijau" aria-hidden="true" />
    <slot />
  </span>
</template>
