<!-- Satu baris info di kartu Akun: label di kiri, nilai tebal di kanan, garis tipis di atas -->
<script setup>
defineProps({
  label: { type: String, required: true },
  nilai: { type: String, required: true },
})
</script>

<template>
  <div class="flex items-center justify-between gap-4 border-t border-garis py-3 text-[15px]">
    <span class="text-ink">{{ label }}</span>
    <span class="text-right text-xs font-bold text-navy">{{ nilai }}</span>
  </div>
</template>
