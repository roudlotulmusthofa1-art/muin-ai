<!-- Chip hijau "↗ [Demo] al-Mukhtasar al-Tajribi 2/145". Klik = buka panel bukti. -->
<script setup>
import { computed } from 'vue'
import { useSesiChat } from '../../composables/useSesiChat'
import { labelSitasi } from '../../data/dataSitasi'

const props = defineProps({
  sitasiId: { type: String, required: true },
})

const { sitasiAktif, bukaBukti } = useSesiChat()

const aktif = computed(() => sitasiAktif.value === props.sitasiId)
</script>

<template>
  <button
    type="button"
    class="ml-1 inline-flex items-center gap-1 rounded-full border px-2.5 py-0.5 align-middle text-xs font-semibold text-hijau transition hover:border-hijau"
    :class="
      aktif ? 'border-hijau bg-hijau-muda ring-2 ring-hijau/20' : 'border-[#b9d8cf] bg-hijau-muda'
    "
    :aria-pressed="aktif"
    @click="bukaBukti(sitasiId)"
  >
    <!-- Ikon panah ↗ (pakai SVG, karena simbol ↗ bisa tampil sebagai emoji di Windows) -->
    <svg
      width="10"
      height="10"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="3"
      stroke-linecap="round"
      stroke-linejoin="round"
      aria-hidden="true"
    >
      <path d="M7 17L17 7M9 7h8v8" />
    </svg>
    {{ labelSitasi(sitasiId) }}
  </button>
</template>
