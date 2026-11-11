<!-- Bagian bawah modal: ringkasan pilihan + tombol Simpan grup & Gunakan pilihan -->
<script setup>
defineProps({
  judul: { type: String, required: true },
  keterangan: { type: String, default: '' },
  pesan: { type: String, default: '' }, // notifikasi kecil, misal "Grup disimpan (demo)"
})

const emit = defineEmits(['simpan', 'gunakan'])
</script>

<template>
  <div class="border-t border-garis bg-white px-5 py-4">
    <div class="flex items-center gap-3">
      <div class="min-w-0 flex-1">
        <p class="text-[13px] font-bold text-navy">{{ judul }}</p>
        <p class="mt-0.5 text-[11px] leading-5 text-ink-soft">
          <span v-if="pesan" class="font-semibold text-hijau">{{ pesan }}</span>
          <span v-else>{{ keterangan }}</span>
        </p>
      </div>

      <button
        type="button"
        class="shrink-0 rounded-xl border border-[#d5c9b8] bg-white px-4 py-3 text-sm font-bold whitespace-nowrap text-navy transition hover:bg-krem-muda"
        @click="emit('simpan')"
      >
        Simpan grup
      </button>

      <button
        type="button"
        class="shrink-0 rounded-xl bg-hijau px-4 py-3 text-sm font-bold whitespace-nowrap text-white shadow-sm transition hover:bg-hijau-tua"
        @click="emit('gunakan')"
      >
        Gunakan pilihan
      </button>
    </div>
  </div>
</template>
