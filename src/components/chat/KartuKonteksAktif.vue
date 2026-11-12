<!-- Kartu "KONTEKS AKTIF" di bawah sidebar: cakupan + pilihan riset yang sedang dipakai -->
<script setup>
import { useSesiChat } from '../../composables/useSesiChat'
import { useRiset } from '../../composables/useRiset'

const { pertanyaanAktif, ringkasCakupan } = useSesiChat()
const { labelTombol } = useRiset()
</script>

<template>
  <div class="rounded-2xl border border-garis bg-kertas px-4 py-4">
    <p class="text-[10px] font-bold tracking-[0.14em] text-ink-soft uppercase">Konteks aktif</p>
    <p v-if="pertanyaanAktif" class="mt-2 text-[13px] leading-5 font-bold text-navy">
      {{ ringkasCakupan.bidang }}<br />
      {{ ringkasCakupan.tugas }}
    </p>
    <p v-else class="mt-2 text-[13px] leading-5 text-ink-soft">Belum ada pertanyaan</p>
    <p class="mt-4 text-xs font-bold text-navy">{{ labelTombol }}</p>
  </div>
</template>
