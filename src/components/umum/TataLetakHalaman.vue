<!--
  Kerangka halaman biasa (Riwayat, Ekspor, Akun):

  ┌ KepalaHalaman (judul kecil + lencana) ─────────────┐
  │   LABEL KECIL                                      │
  │   Judul Besar                                      │
  │   Deskripsi                                        │
  │   <slot> ← isi khusus tiap halaman                 │
  └────────────────────────────────────────────────────┘

  Dengan komponen ini, tiap halaman cukup mengisi teks dan isinya saja.
-->
<script setup>
import KepalaHalaman from './KepalaHalaman.vue'

defineProps({
  judul: { type: String, required: true }, // judul di kepala halaman, contoh "Riwayat 3 Hari"
  subjudul: { type: String, default: '' }, // teks kecil di bawah judul kepala
  label: { type: String, default: '' }, // label kecil huruf kapital di atas judul besar
  judulBesar: { type: String, required: true }, // contoh "Hasil yang masih hidup"
  deskripsi: { type: String, default: '' },
})
</script>

<template>
  <!-- h-full + min-h-0: hanya bagian isi yang di-scroll, kepala halaman tetap di atas -->
  <div class="flex h-full flex-col bg-[#F7F2E8]">
    <KepalaHalaman :judul="judul" :subjudul="subjudul" />

    <main class="min-h-0 flex-1 overflow-y-auto px-4 sm:px-8">
      <div class="mx-auto max-w-[844px] pt-10 pb-16">
        <p v-if="label" class="text-[11px] font-bold tracking-[0.14em] text-ink-soft uppercase">
          {{ label }}
        </p>
        <h2 class="mt-3 text-3xl leading-tight font-bold tracking-tight text-navy sm:text-[44px]">
          {{ judulBesar }}
        </h2>
        <p v-if="deskripsi" class="mt-3 text-[15px] text-ink-soft">{{ deskripsi }}</p>

        <!-- Isi khusus tiap halaman -->
        <div class="mt-8">
          <slot />
        </div>
      </div>
    </main>
  </div>
</template>
