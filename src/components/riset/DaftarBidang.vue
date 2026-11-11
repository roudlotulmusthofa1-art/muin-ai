<!-- Isi tab "Bidang & Mazhab" -->
<script setup>
import { useRiset } from '../../composables/useRiset'
import { dataBidang } from '../../data/dataBidang'
import { dataKitab } from '../../data/dataKitab'
import GrupKitab from './GrupKitab.vue'
import BidangTidakAktif from './BidangTidakAktif.vue'

const { hitungTerpilih } = useRiset()

function kitabDiBidang(bidangId) {
  return dataKitab.filter((k) => k.bidangId === bidangId)
}

function labelJumlah(bidangId) {
  const kitab = kitabDiBidang(bidangId)
  return `${hitungTerpilih(kitab.map((k) => k.id))} dari ${kitab.length} kitab`
}
</script>

<template>
  <div class="space-y-2">
    <template v-for="bidang in dataBidang" :key="bidang.id">
      <GrupKitab
        v-if="bidang.status === 'aktif'"
        :judul="bidang.nama"
        :keterangan="bidang.keterangan"
        :label-jumlah="labelJumlah(bidang.id)"
        :kitab="kitabDiBidang(bidang.id)"
      />
      <BidangTidakAktif v-else :bidang="bidang" />
    </template>
  </div>
</template>
