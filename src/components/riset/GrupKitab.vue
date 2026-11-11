<!--
  Kartu grup yang bisa dibuka/ditutup, berisi daftar BarisKitab.
  Dipakai untuk: satu bidang (tab Bidang), satu mu'allif (tab Mu'allif),
  dan "Daftar kitab Fikih · Syafi'i" (tab Kitab, tanpa centang grup).
-->
<script setup>
import { ref, computed } from 'vue'
import { useRiset } from '../../composables/useRiset'
import { namaMuallif } from '../../data/dataMuallif'
import KotakCentang from './KotakCentang.vue'
import IkonPanah from './IkonPanah.vue'
import BarisKitab from './BarisKitab.vue'

const props = defineProps({
  judul: { type: String, required: true },
  keterangan: { type: String, default: '' },
  labelJumlah: { type: String, default: '' }, // contoh: "6 dari 8 kitab"
  kitab: { type: Array, required: true },
  pakaiCentang: { type: Boolean, default: true }, // tampilkan centang grup di kiri
  paksaBuka: { type: Boolean, default: false }, // misal saat sedang mencari
})

const { draf, bisaDiubah, modeRadio, bisaPilihGrup, apakahTerpilih, keadaanGrup, ubahKitab, ubahGrup } =
  useRiset()

const terbuka = ref(false)
const tampilIsi = computed(() => terbuka.value || props.paksaBuka)

const idKitab = computed(() => props.kitab.map((k) => k.id))
const keadaan = computed(() => keadaanGrup(idKitab.value))

// Filter "Hanya sumber yang saya pilih"
const kitabTampil = computed(() =>
  draf.value.hanyaPilihan ? props.kitab.filter((k) => apakahTerpilih(k.id)) : props.kitab,
)

const ariaCentang = computed(() =>
  keadaan.value === 'penuh' ? 'true' : keadaan.value === 'sebagian' ? 'mixed' : 'false',
)
</script>

<template>
  <div class="overflow-hidden rounded-xl border border-garis bg-white">
    <!-- KEPALA GRUP -->
    <div class="flex items-center gap-3 px-3 py-3 transition" :class="tampilIsi ? 'bg-hijau-muda/50' : ''">
      <!-- Centang grup: pilih / lepas semua kitab di grup ini -->
      <button
        v-if="pakaiCentang"
        type="button"
        role="checkbox"
        :aria-checked="ariaCentang"
        :aria-label="`Pilih semua kitab ${judul}`"
        :disabled="!bisaPilihGrup"
        class="shrink-0 disabled:cursor-default"
        @click="ubahGrup(idKitab)"
      >
        <KotakCentang :keadaan="keadaan" />
      </button>

      <!-- Klik judul untuk buka/tutup (tidak mengubah pilihan) -->
      <button
        type="button"
        class="flex min-w-0 flex-1 items-center gap-3 text-left"
        :aria-expanded="tampilIsi"
        @click="terbuka = !terbuka"
      >
        <div class="min-w-0 flex-1">
          <p class="truncate text-[15px] font-bold text-navy">{{ judul }}</p>
          <p v-if="keterangan" class="truncate text-xs text-ink-soft">{{ keterangan }}</p>
        </div>
        <span class="shrink-0 text-[11px] font-semibold text-ink-soft">{{ labelJumlah }}</span>
        <IkonPanah :terbuka="tampilIsi" />
      </button>
    </div>

    <!-- ISI GRUP -->
    <div v-if="tampilIsi" class="border-t border-garis">
      <BarisKitab
        v-for="k in kitabTampil"
        :key="k.id"
        :kitab="k"
        :nama-muallif="namaMuallif(k.muallifId)"
        :terpilih="apakahTerpilih(k.id)"
        :radio="modeRadio"
        :terkunci="!bisaDiubah"
        :menjorok="pakaiCentang"
        @ubah="ubahKitab(k.id)"
      />
      <p v-if="kitabTampil.length === 0" class="py-4 text-center text-xs text-ink-faint">
        Tidak ada kitab yang cocok.
      </p>
    </div>
  </div>
</template>
