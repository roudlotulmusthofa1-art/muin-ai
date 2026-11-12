<!-- Judul modal + tombol tutup (✕) -->
<script setup>
const emit = defineEmits(['tutup'])
</script>

<template>
  <div class="flex items-start justify-between gap-4 border-b border-garis px-5 pt-5 pb-4">
    <div>
      <p class="text-xs font-bold tracking-[0.15em] text-ink-soft uppercase">Atur Riset</p>
      <h2 class="mt-1 text-[22px] leading-tight font-bold text-navy">Pilih sumber penelitian</h2>
      <p class="mt-1 text-xs text-ink-soft">Tiga pintu, satu daftar akhir yang dapat diperiksa.</p>
    </div>

    <button
      type="button"
      class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl border border-garis bg-white text-navy transition hover:bg-krem-muda focus-visible:ring-2 focus-visible:ring-[#b8d8cf] focus-visible:outline-none"
      aria-label="Tutup"
      @click="emit('tutup')"
    >
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">
        <path d="M6 6l12 12M18 6L6 18" />
      </svg>
    </button>
  </div>
</template>
