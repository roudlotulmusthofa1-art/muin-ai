<!--
  Daftar kotak centang untuk memilih hasil yang akan diekspor.

  v-model → array berisi id hasil yang dicentang, contoh ['redaksi-syarat-akad']
  defineModel() adalah cara singkat Vue untuk membuat v-model di komponen sendiri.
-->
<script setup>
defineProps({
  pilihan: { type: Array, required: true }, // daftar hasil: [{ id, judul }]
})

const terpilih = defineModel({ type: Array, required: true })
</script>

<template>
  <div class="space-y-2">
    <label
      v-for="hasil in pilihan"
      :key="hasil.id"
      class="flex cursor-pointer items-center gap-3 rounded-xl border border-garis bg-krem-muda px-4 py-3 text-[15px] text-ink transition hover:bg-white"
    >
      <!-- v-model pada checkbox + :value → Vue otomatis menambah/menghapus id di array -->
      <input v-model="terpilih" type="checkbox" :value="hasil.id" class="h-4 w-4 accent-[#1a6ee0]" />
      {{ hasil.judul }}
    </label>
  </div>
</template>
