<!-- Bilah "Fikih › Syafi’i › Riset Masalah › Pilih Sumber · 6 kitab ......... Atur Riset" -->
<script setup>
import { computed } from 'vue'
import { useSesiChat } from '../../composables/useSesiChat'
import { useRiset } from '../../composables/useRiset'

const { bagianCakupan, sedangBerjalan } = useSesiChat()
const { labelTombol, bukaModal } = useRiset()

// Remah roti (breadcrumb): bagian cakupan + pilihan riset
const remah = computed(() => [...bagianCakupan.value, labelTombol.value])
</script>

<template>
  <nav
    aria-label="Konteks riset"
    class="flex items-center justify-between gap-4 rounded-2xl border border-garis bg-kertas px-4 py-3.5"
  >
    <ol class="flex min-w-0 flex-wrap items-center gap-x-2 gap-y-1 text-[13px] font-bold text-navy">
      <li v-for="(bagian, i) in remah" :key="i" class="flex items-center gap-2">
        <span v-if="i > 0" class="text-[10px] text-ink-faint" aria-hidden="true">›</span>
        {{ bagian }}
      </li>
    </ol>

    <!-- Dikunci saat riset berjalan ("Konteks dan selector dikunci") -->
    <button
      type="button"
      class="shrink-0 text-[13px] font-bold text-navy transition hover:text-hijau disabled:cursor-not-allowed disabled:opacity-40"
      :disabled="sedangBerjalan"
      @click="bukaModal"
    >
      Atur Riset
    </button>
  </nav>
</template>
