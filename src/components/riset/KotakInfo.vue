<!--
  Kotak keterangan.
  varian 'hijau': judul tebal di baris sendiri (kotak "Pencarian terstruktur")
  varian 'krem' : judul tebal menyatu dengan isi (keterangan per tab)
-->
<script setup>
defineProps({
  varian: { type: String, default: 'krem' },
  judul: { type: String, required: true },
  isi: { type: String, default: '' },
})
</script>

<template>
  <div v-if="varian === 'hijau'" class="rounded-xl border border-[#b9d8cf] bg-[#f0f5f0] px-4 py-3">
    <p class="text-[13px] font-bold text-hijau">{{ judul }}</p>
    <p class="mt-1 text-xs leading-5 text-ink-soft">{{ isi }}</p>
  </div>

  <div v-else class="rounded-xl border border-garis bg-krem-muda px-4 py-3">
    <p class="text-xs leading-5 text-ink-soft">
      <strong class="font-bold text-ink">{{ judul }}</strong>
      {{ isi }}
    </p>
  </div>
</template>
