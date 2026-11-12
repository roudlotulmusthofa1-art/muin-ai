<!-- Tampilan saat riset selesai: statistik, peringatan, ringkasan, peta temuan, keterbatasan -->
<script setup>
import { computed } from 'vue'
import { useSesiChat } from '../../composables/useSesiChat'
import { jawabanDemo } from '../../data/dataJawaban'
import ChipSitasi from './ChipSitasi.vue'

const { pertanyaanAktif, teksBesar } = useSesiChat()

const statistik = computed(() => [
  `${pertanyaanAktif.value.jumlahKitab} kitab pilihan diperiksa silang`,
  ...jawabanDemo.statistikTambahan,
])
</script>

<template>
  <article class="space-y-7" :class="teksBesar ? 'text-[17px]' : 'text-[15px]'">
    <!-- BARIS STATISTIK -->
    <div
      class="flex flex-wrap items-center gap-x-3 gap-y-1 border-b border-garis pb-4 text-xs text-ink-soft"
    >
      <span class="font-bold text-hijau">Riset selesai</span>
      <span v-for="item in statistik" :key="item">{{ item }}</span>
    </div>

    <!-- PERINGATAN DATA DEMO -->
    <div
      class="rounded-xl border border-[#ecd28f] bg-[#fdf6dc] px-4 py-3 text-[13px] leading-6 text-[#5b4a1c]"
    >
      <strong class="font-bold">{{ jawabanDemo.peringatan.judul }}</strong>
      {{ jawabanDemo.peringatan.isi }}
    </div>

    <section>
      <h3 class="text-[22px] font-bold text-navy">Ringkasan</h3>
      <p class="mt-3 leading-7 text-ink">{{ jawabanDemo.ringkasan }}</p>
    </section>

    <section>
      <h3 class="text-[22px] font-bold text-navy">Peta temuan demonstrasi</h3>
      <ol class="mt-3 list-decimal space-y-3 pl-5 leading-7 text-ink">
        <li v-for="temuan in jawabanDemo.temuan" :key="temuan.sitasiId">
          {{ temuan.teks }}
          <ChipSitasi :sitasi-id="temuan.sitasiId" />
        </li>
      </ol>
    </section>

    <section>
      <h3 class="text-[22px] font-bold text-navy">Keterbatasan</h3>
      <p class="mt-3 leading-7 text-ink">{{ jawabanDemo.keterbatasan }}</p>
    </section>
  </article>
</template>
