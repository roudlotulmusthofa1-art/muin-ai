<!--
  Kerangka kartu status. Dipakai oleh 4 kartu:
  StatusBerjalan (netral), StatusBelumCukup (kuning), StatusGangguan (merah), StatusDibatalkan (netral).

  props:
    nada      : 'netral' | 'kuning' | 'merah'   → warna kartu
    ikon      : 'putar' | 'segitiga' | 'seru'   → ikon kecil di kiri label
    label     : teks kecil huruf besar, contoh "PEKERJAAN AKTIF"
    judul     : teks besar, contoh "Riset sedang berjalan"
    deskripsi : kalimat penjelasan
  slot (tempat "menitipkan" isi dari luar):
    #catatan  : teks kecil tepat di bawah deskripsi (contoh: kode bantuan)
    default   : isi utama (contoh: daftar langkah)
    #aksi     : deretan tombol di bawah
-->
<script setup>
defineProps({
  nada: { type: String, default: 'netral' },
  ikon: { type: String, default: 'putar' },
  label: { type: String, required: true },
  judul: { type: String, required: true },
  deskripsi: { type: String, default: '' },
})

const kelasNada = {
  netral: 'border-[#b9d8cf] bg-kertas',
  kuning: 'border-[#ecd28f] bg-[#fdf9ee]',
  merah: 'border-[#f0b8b8] bg-[#fdeeee]',
}
</script>

<template>
  <section class="rounded-2xl border px-6 py-6" :class="kelasNada[nada]" :aria-busy="ikon === 'putar'">
    <div class="flex gap-3">
      <!-- IKON -->
      <span class="mt-0.5 flex h-4 w-4 shrink-0 items-center justify-center text-navy" aria-hidden="true">
        <span
          v-if="ikon === 'putar'"
          class="h-3.5 w-3.5 animate-spin rounded-full border-2 border-[#b9d8cf] border-t-hijau"
        />
        <svg v-else-if="ikon === 'segitiga'" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round">
          <path d="M12 4L22 20H2z" />
        </svg>
        <span v-else class="text-sm leading-none font-bold">!</span>
      </span>

      <!-- TEKS -->
      <div class="min-w-0 flex-1">
        <p class="text-[11px] font-bold tracking-[0.14em] text-ink-soft uppercase">{{ label }}</p>
        <h3 class="mt-2 text-xl font-bold text-navy">{{ judul }}</h3>
        <p v-if="deskripsi" class="mt-2 text-[15px] leading-relaxed text-ink-soft">{{ deskripsi }}</p>
        <div v-if="$slots.catatan" class="mt-2">
          <slot name="catatan" />
        </div>
      </div>
    </div>

    <div v-if="$slots.default" class="mt-5">
      <slot />
    </div>

    <div v-if="$slots.aksi" class="mt-5 flex flex-wrap gap-2.5">
      <slot name="aksi" />
    </div>
  </section>
</template>
