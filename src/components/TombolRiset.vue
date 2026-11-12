<!--
  Tombol di atas kolom tanya. Klik = buka modal "Atur Riset".
  Tulisannya mengikuti pilihan riset yang sedang dipakai.
-->
<script setup>
import { useRiset } from '../composables/useRiset'

const { labelTombol, bukaModal, modalTerbuka } = useRiset()
</script>

<template>
  <button
    type="button"
    class="flex max-w-full items-center gap-1.5 rounded-full border border-black/5 bg-white px-4 py-2 text-[13px] font-semibold text-emerald-brand shadow-chip transition hover:border-navy/20"
    aria-haspopup="dialog"
    :aria-expanded="modalTerbuka"
    @click="bukaModal"
  >
    <svg class="shrink-0" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z" />
      <path d="M4 20.5V5.5M20 18v3H6.5" />
    </svg>
    <span class="max-w-[16rem] truncate">{{ labelTombol }}</span>
    <svg class="shrink-0 text-ink-faint" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
      <path d="M6 9l6 6 6-6" />
    </svg>
  </button>
</template>
