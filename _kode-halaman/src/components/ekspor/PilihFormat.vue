<!--
  Pilihan format berkas (tombol radio berbentuk kotak).
  v-model → 'pdf' atau 'markdown'
-->
<script setup>
const format = defineModel({ type: String, required: true })

const daftarFormat = [
  { id: 'pdf', label: 'PDF' },
  { id: 'markdown', label: 'Markdown' },
]
</script>

<template>
  <div class="flex flex-wrap gap-2.5" role="radiogroup" aria-label="Format berkas">
    <label
      v-for="f in daftarFormat"
      :key="f.id"
      class="flex min-w-32 cursor-pointer items-center gap-3 rounded-xl border bg-krem-muda px-4 py-3 text-[15px] text-ink transition hover:bg-white"
      :class="format === f.id ? 'border-[#c9bda9]' : 'border-garis'"
    >
      <!-- name yang sama → hanya satu yang bisa dipilih -->
      <input v-model="format" type="radio" name="format-ekspor" :value="f.id" class="h-4 w-4 accent-[#1a6ee0]" />
      {{ f.label }}
    </label>
  </div>
</template>
