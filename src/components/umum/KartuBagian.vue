<!--
  Kartu putih: judul + deskripsi + isi bebas (slot).
  Dipakai di halaman Ekspor ("1. Pilih hasil", "2. Pilih format", ...) dan Akun.

  nada: 'netral' (garis krem, default) | 'bahaya' (garis merah, untuk aksi seperti "Keluar")
-->
<script setup>
defineProps({
  judul: { type: String, required: true },
  deskripsi: { type: String, default: '' },
  nada: { type: String, default: 'netral' },
})
</script>

<template>
  <section
    class="rounded-2xl border bg-kertas px-5 py-5 sm:px-6"
    :class="nada === 'bahaya' ? 'border-[#f0b8b8]' : 'border-garis'"
  >
    <h3 class="text-[15px] font-bold text-navy">{{ judul }}</h3>
    <p v-if="deskripsi" class="mt-1.5 text-xs text-ink-soft">{{ deskripsi }}</p>

    <!-- Isi kartu (kalau ada), dikirim dari halaman yang memakai komponen ini -->
    <div v-if="$slots.default" class="mt-3">
      <slot />
    </div>
  </section>
</template>
