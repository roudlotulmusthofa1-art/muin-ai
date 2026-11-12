<!--
  Tombol serbaguna. Dipakai di semua kartu status dan panel bukti.
  varian:
    'utama' → hijau penuh   (contoh: "Ubah sumber", "Coba lagi gratis")
    'garis' → putih bergaris (contoh: "Ubah pertanyaan", "Salin teks persis")
    'bahaya'→ merah muda     (contoh: "Batalkan")
  Atribut lain seperti @click dan disabled otomatis diteruskan ke <button>.
-->
<script setup>
defineProps({
  varian: { type: String, default: 'garis' },
  type: { type: String, default: 'button' },
})
</script>

<template>
  <button
    :type="type"
    class="inline-flex items-center justify-center gap-1.5 rounded-xl px-4 py-2.5 text-sm font-bold whitespace-nowrap transition disabled:cursor-not-allowed disabled:opacity-50"
    :class="{
      'bg-hijau text-white shadow-sm hover:bg-hijau-tua': varian === 'utama',
      'border border-[#d5c9b8] bg-white text-navy hover:bg-krem-muda': varian === 'garis',
      'border border-[#f0b8b8] bg-[#fdeeee] text-[#a23a3a] hover:bg-[#fbe2e2]': varian === 'bahaya',
    }"
  >
    <slot />
  </button>
</template>
