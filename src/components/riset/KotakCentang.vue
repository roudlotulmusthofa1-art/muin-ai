<!--
  Tampilan centang (hanya gambar, tidak bisa diklik sendiri).
  Yang bisa diklik adalah tombol induknya.
  keadaan: 'kosong' | 'sebagian' (−) | 'penuh' (✓)
  bentuk : 'kotak' (checkbox) | 'bulat' (radio)
-->
<script setup>
defineProps({
  keadaan: { type: String, default: 'kosong' },
  bentuk: { type: String, default: 'kotak' },
})
</script>

<template>
  <!-- RADIO (bulat) -->
  <span
    v-if="bentuk === 'bulat'"
    aria-hidden="true"
    class="flex h-5 w-5 shrink-0 items-center justify-center rounded-full border-2 bg-white transition"
    :class="keadaan === 'penuh' ? 'border-navy' : 'border-ink-faint'"
  >
    <span v-if="keadaan === 'penuh'" class="h-2.5 w-2.5 rounded-full bg-navy" />
  </span>

  <!-- CHECKBOX (kotak) -->
  <span
    v-else
    aria-hidden="true"
    class="flex h-5 w-5 shrink-0 items-center justify-center rounded border-2 transition"
    :class="keadaan === 'kosong' ? 'border-ink-faint bg-white' : 'border-hijau bg-hijau text-white'"
  >
    <svg
      v-if="keadaan === 'penuh'"
      width="14"
      height="14"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="3"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path d="M5 12.5l4.5 4.5L19 7.5" />
    </svg>
    <span v-else-if="keadaan === 'sebagian'" class="h-0.5 w-2.5 rounded-full bg-white" />
  </span>
</template>
