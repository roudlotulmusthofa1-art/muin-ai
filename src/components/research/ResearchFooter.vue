<script setup>
const emit = defineEmits(['close'])

function closeMenu() {
  emit('close')
}
</script>

<template>
  <div
    class="border-t border-[#ddd5c8]
           bg-[#fffdfa]
           px-5 py-4"
  >

    <div class="flex items-center gap-4">

      <div class="flex-1">

        <p
          class="text-[13px]
                 font-bold
                 text-[#172c46]"
        >
          Otomatis · Muin memilih sumber relevan
        </p>

        <p
          class="mt-1
                 text-[11px]
                 leading-5
                 text-[#73776f]"
        >
          Bukan hasil pertama; daftar akhir sumber tetap dapat diperiksa.
        </p>

      </div>

      <button
        type="button"
        class="px-7 py-3
               rounded-xl
               border border-[#d5c9b8]
               bg-white
               text-[#172c46]
               font-bold
               text-sm
               hover:bg-[#faf7f0]
               transition"
        @click="closeMenu"
      >
        Simpan grup
      </button>

      <button
        type="button"
        class="px-7 py-3
               rounded-xl
               bg-[#087f65]
               text-white
               font-bold
               text-sm
               hover:bg-[#066b55]
               transition
               shadow-sm"
        @click="closeMenu"
      >
        Gunakan<br />
        pilihan
      </button>

    </div>

  </div>
</template>