<!-- Kartu bidang yang belum bisa dipilih (nonaktif / belum tersedia). Hanya tampilan. -->
<script setup>
defineProps({
  bidang: { type: Object, required: true },
})
</script>

<template>
  <div class="flex items-center gap-3 rounded-xl border border-garis bg-white px-3 py-3">
    <!-- Ikon: lingkaran kosong (nonaktif) atau garis (belum tersedia) -->
    <span class="flex h-5 w-5 shrink-0 items-center justify-center" aria-hidden="true">
      <span v-if="bidang.status === 'nonaktif'" class="h-3 w-3 rounded-full border-[1.5px] border-navy" />
      <span v-else class="h-0.5 w-3.5 bg-navy" />
    </span>

    <div class="min-w-0 flex-1">
      <p class="truncate text-[15px] font-bold text-navy">{{ bidang.nama }}</p>
      <p class="truncate text-xs text-ink-soft">{{ bidang.keterangan }}</p>
    </div>

    <span
      class="shrink-0 text-[11px] font-semibold"
      :class="bidang.status === 'belum-tersedia' ? 'text-[#a36a19]' : 'text-ink-soft'"
    >
      {{ bidang.labelJumlah }}
    </span>
  </div>
</template>
