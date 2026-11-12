<!-- Tabel Judul / Mu'allif / Bidang / Edisi / Lokasi / Provenans di panel bukti -->
<script setup>
import { computed } from 'vue'

const props = defineProps({
  sitasi: { type: Object, required: true },
})

const baris = computed(() => [
  { label: 'Judul', nilai: props.sitasi.judul },
  { label: 'Mu’allif', nilai: props.sitasi.muallif },
  { label: 'Bidang', nilai: props.sitasi.bidang },
  { label: 'Edisi', nilai: props.sitasi.edisi },
  { label: 'Lokasi', nilai: props.sitasi.lokasi },
  { label: 'Provenans', nilai: props.sitasi.provenans },
])
</script>

<template>
  <dl class="divide-y divide-garis border-y border-garis text-xs">
    <div v-for="item in baris" :key="item.label" class="grid grid-cols-[110px_1fr] gap-3 py-2.5">
      <dt class="text-ink-soft">{{ item.label }}</dt>
      <dd class="leading-5 font-semibold text-navy">{{ item.nilai }}</dd>
    </div>
  </dl>
</template>
