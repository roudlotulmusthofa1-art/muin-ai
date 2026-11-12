<!--
  Modal "Atur Riset". Ini induk yang menyusun semua bagian modal.
  Semua pilihan disimpan di composables/useRiset.js (bukan di sini),
  jadi tidak hilang saat modal ditutup.
-->
<script setup>
import { ref, watch, onMounted, onBeforeUnmount } from 'vue'
import { useRiset } from '../../composables/useRiset'
import KepalaModal from './KepalaModal.vue'
import TabMode from './TabMode.vue'
import KotakInfo from './KotakInfo.vue'
import TabSumber from './TabSumber.vue'
import FilterPilihan from './FilterPilihan.vue'
import DaftarBidang from './DaftarBidang.vue'
import DaftarMuallif from './DaftarMuallif.vue'
import DaftarKitab from './DaftarKitab.vue'
import KakiModal from './KakiModal.vue'

const { draf, ringkasan, gantiMode, tutupModal, gunakanPilihan } = useRiset()

// Tab sumber yang sedang dibuka: 'bidang' | 'muallif' | 'kitab'
const tabSumber = ref(draf.value.mode === 'satu-kitab' ? 'kitab' : 'bidang')

// Studi Satu Kitab → langsung tampilkan tab Kitab
watch(
  () => draf.value.mode,
  (mode) => {
    if (mode === 'satu-kitab') tabSumber.value = 'kitab'
  },
)

const infoTab = {
  bidang: {
    judul: 'Mulai dari bidang/fann.',
    isi: 'Memilih satu blok memilih seluruh kitab eligible di bawahnya. Anda tetap dapat mengecualikan kitab tertentu.',
  },
  muallif: {
    judul: 'Urutan navigasi:',
    isi: 'wafat terdahulu menuju kemudian. Ini bukan ranking otoritas ilmiah.',
  },
}

// "Simpan grup" masih demo: cukup tampilkan pesan 2 detik
const pesanSimpan = ref('')
let timer = null
function simpanGrup() {
  pesanSimpan.value = 'Grup disimpan (demo)'
  clearTimeout(timer)
  timer = setTimeout(() => (pesanSimpan.value = ''), 2000)
}

// Tombol Esc menutup modal
function tekanTombol(e) {
  if (e.key === 'Escape') tutupModal()
}
onMounted(() => document.addEventListener('keydown', tekanTombol))
onBeforeUnmount(() => {
  document.removeEventListener('keydown', tekanTombol)
  clearTimeout(timer)
})
</script>

<template>
  <!-- LATAR GELAP: klik di luar panel = tutup -->
  <div class="fixed inset-0 z-50 bg-navy/40 backdrop-blur-[2px]" @click.self="tutupModal">
    <!-- PANEL -->
    <aside
      role="dialog"
      aria-modal="true"
      aria-label="Atur riset"
      class="absolute top-7 right-0 bottom-0 flex w-full max-w-155 flex-col overflow-hidden rounded-l-[22px] bg-kertas shadow-2xl"
    >
      <KepalaModal @tutup="tutupModal" />

      <!-- ISI (bisa di-scroll) -->
      <div class="flex-1 space-y-3 overflow-y-auto px-4 py-3">
        <TabMode :model-value="draf.mode" @update:model-value="gantiMode" />

        <KotakInfo
          varian="hijau"
          judul="Pencarian terstruktur, bukan acak."
          isi="Muin tidak berhenti pada kitab yang paling dulu cocok. Sumber disusun menurut bidang, mazhab, peran kitab, dan kebijakan ilmiah domain, lalu diperiksa silang."
        />

        <TabSumber v-model="tabSumber" />

        <FilterPilihan v-model="draf.hanyaPilihan" />

        <template v-if="tabSumber === 'bidang'">
          <KotakInfo :judul="infoTab.bidang.judul" :isi="infoTab.bidang.isi" />
          <DaftarBidang />
        </template>

        <template v-else-if="tabSumber === 'muallif'">
          <KotakInfo :judul="infoTab.muallif.judul" :isi="infoTab.muallif.isi" />
          <DaftarMuallif />
        </template>

        <DaftarKitab v-else />
      </div>

      <KakiModal
        :judul="ringkasan.judul"
        :keterangan="ringkasan.keterangan"
        :pesan="pesanSimpan"
        @simpan="simpanGrup"
        @gunakan="gunakanPilihan"
      />
    </aside>
  </div>
</template>
