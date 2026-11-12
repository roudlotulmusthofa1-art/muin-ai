<!--
  Panel kanan "Bukti dan konteks". Muncul saat chip sitasi diklik.
  Layar besar (lg): panel di samping jawaban. Layar kecil: menutupi seluruh layar.
-->
<script setup>
import { computed, onMounted, onBeforeUnmount } from 'vue'
import { useSesiChat } from '../../composables/useSesiChat'
import { useSalin } from '../../composables/useSalin'
import { detailSitasi } from '../../data/dataSitasi'
import InfoSitasi from './InfoSitasi.vue'
import PratinjauHalaman from './PratinjauHalaman.vue'
import TombolAksi from '../umum/TombolAksi.vue'

const { sitasiAktif, tutupBukti } = useSesiChat()
const { salin, labelTombol } = useSalin()

const sitasi = computed(() => detailSitasi(sitasiAktif.value))

const teksPersis = computed(() => {
  const t = sitasi.value.teks
  return t.sebelum + t.sorot + t.sesudah
})

function salinTeks() {
  salin(teksPersis.value, 'teks')
}

function salinDenganSitasi() {
  salin(`${teksPersis.value}\n\n— ${sitasi.value.label} (data demo, tidak terverifikasi)`, 'sitasi')
}

// Tombol Esc menutup panel
function tekanTombol(e) {
  if (e.key === 'Escape') tutupBukti()
}
onMounted(() => document.addEventListener('keydown', tekanTombol))
onBeforeUnmount(() => document.removeEventListener('keydown', tekanTombol))
</script>

<template>
  <aside
    aria-label="Bukti dan konteks"
    class="fixed inset-0 z-40 flex flex-col gap-5 overflow-y-auto bg-[#f5f0e5] px-6 py-6 lg:static lg:z-auto lg:w-[430px] lg:shrink-0 lg:border-l lg:border-black/10"
  >
    <!-- KEPALA PANEL -->
    <div class="flex items-start justify-between gap-4">
      <div>
        <span
          class="inline-block rounded-full border border-[#ecd28f] bg-[#fdf1c7] px-2.5 py-1 text-[10px] font-bold tracking-wide text-[#6b5413] uppercase"
        >
          Data demo · tidak terverifikasi
        </span>
        <h2 class="mt-2 text-xl font-bold text-navy">Bukti dan konteks</h2>
      </div>
      <button
        type="button"
        class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl border border-garis bg-white text-navy transition hover:bg-krem-muda"
        aria-label="Tutup panel bukti"
        @click="tutupBukti"
      >
        <svg
          width="14"
          height="14"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2.2"
          stroke-linecap="round"
        >
          <path d="M6 6l12 12M18 6L6 18" />
        </svg>
      </button>
    </div>

    <InfoSitasi :sitasi="sitasi" />

    <!-- :key membuat pratinjau "mulai dari awal" setiap kali sitasi berganti -->
    <PratinjauHalaman :key="sitasi.id" :sitasi="sitasi" />

    <div class="flex flex-wrap gap-2.5 pb-8">
      <TombolAksi @click="salinTeks">{{ labelTombol('teks', 'Salin teks persis') }}</TombolAksi>
      <TombolAksi @click="salinDenganSitasi">{{
        labelTombol('sitasi', 'Salin teks + sitasi')
      }}</TombolAksi>
    </div>
  </aside>
</template>
