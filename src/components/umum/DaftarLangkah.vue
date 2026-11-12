<!--
  Daftar berikon. Dipakai di kartu "Pekerjaan aktif" dan "Kesimpulan ditahan".
  items: [{ status, teks, label? }]
    status: 'selesai' (✓) | 'berjalan' (•) | 'menunggu' (○) | 'peringatan' (!) | 'catatan' (—)
    label : teks tebal opsional di depan, contoh "Yang diperiksa:"
-->
<script setup>
defineProps({
  items: { type: Array, required: true },
})

const ikon = { selesai: '✓', berjalan: '•', menunggu: '○', peringatan: '!', catatan: '—' }

const warnaIkon = {
  selesai: 'text-hijau',
  berjalan: 'text-ink-soft',
  menunggu: 'text-ink-soft',
  peringatan: 'text-navy font-bold',
  catatan: 'text-navy',
}

// Teks untuk pembaca layar (orang tunanetra), karena ikon ✓ ○ tidak dibacakan
const namaStatus = {
  selesai: 'Selesai:',
  berjalan: 'Sedang berjalan:',
  menunggu: 'Menunggu:',
  peringatan: 'Perhatian:',
  catatan: 'Catatan:',
}

// Item tanpa label yang sudah selesai ditulis hijau (seperti di foto "Pekerjaan aktif")
function warnaTeks(item) {
  if (!item.label && item.status === 'selesai') return 'text-hijau'
  return 'text-ink-soft'
}
</script>

<template>
  <ul class="space-y-3">
    <li v-for="(item, i) in items" :key="i" class="flex items-start gap-3 text-[15px] leading-6">
      <span class="w-4 shrink-0 text-center" :class="warnaIkon[item.status]" aria-hidden="true">
        {{ ikon[item.status] }}
      </span>
      <span :class="warnaTeks(item)">
        <span class="sr-only">{{ namaStatus[item.status] }}</span>
        <strong v-if="item.label" class="font-bold text-ink">{{ item.label }}</strong>
        {{ item.teks }}
      </span>
    </li>
  </ul>
</template>
