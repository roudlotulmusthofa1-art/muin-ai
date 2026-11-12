<!-- Isi tab "Mu'allif": urut dari wafat terdahulu -->
<script setup>
import { computed } from 'vue'
import { useRiset } from '../../composables/useRiset'
import { dataMuallif } from '../../data/dataMuallif'
import { dataKitab } from '../../data/dataKitab'
import GrupKitab from './GrupKitab.vue'

const { draf, hitungTerpilih } = useRiset()

function kitabKarya(muallifId) {
  return dataKitab.filter((k) => k.muallifId === muallifId)
}

function jumlahTerpilih(muallifId) {
  return hitungTerpilih(kitabKarya(muallifId).map((k) => k.id))
}

const muallifTampil = computed(() => {
  const urut = [...dataMuallif].sort((a, b) => a.tahunWafat - b.tahunWafat)
  // Filter "Hanya sumber yang saya pilih": sembunyikan mu'allif tanpa kitab terpilih
  return draf.value.hanyaPilihan ? urut.filter((m) => jumlahTerpilih(m.id) > 0) : urut
})
</script>

<template>
  <div class="space-y-2">
    <GrupKitab
      v-for="muallif in muallifTampil"
      :key="muallif.id"
      :judul="muallif.nama"
      :keterangan="muallif.keterangan"
      :label-jumlah="`${jumlahTerpilih(muallif.id)} dari ${kitabKarya(muallif.id).length}`"
      :kitab="kitabKarya(muallif.id)"
    />
    <p v-if="muallifTampil.length === 0" class="py-6 text-center text-xs text-ink-faint">
      Belum ada mu’allif yang dipilih.
    </p>
  </div>
</template>
