<script setup>
const emit = defineEmits(['close'])

function closeMenu() {
  emit('close')
}
</script>

<template>
  <div class="px-5 pt-5 pb-4 border-b border-[#ddd6c9]">

    <div class="flex items-start justify-between">

      <div>

        <p
          class="text-[12px] font-bold
                 tracking-[0.15em]
                 text-[#6b706b]
                 uppercase"
        >
          ATUR RISET
        </p>

        <h2
          class="mt-1 text-[22px]
                 leading-tight
                 font-bold
                 text-[#162b49]"
        >
          Pilih sumber penelitian
        </h2>

        <p
          class="mt-1 text-[12px]
                 text-[#777a75]"
        >
          Tiga pintu, satu daftar akhir yang dapat diperiksa.
        </p>

      </div>

      <!-- CLOSE -->
      <button
        type="button"
        class="w-12 h-12
                rounded-2xl
                border-2 border-[#b8d8cf]
                bg-white
                text-[#162b49]
                flex items-center justify-center
                transition"
        aria-label="Tutup"
        @click="closeMenu"
      >
        <span class="text-xl font-light bg-amber-50
          border-2 border-gray-100 hover:border-gray-300 
          py-1 px-3 rounded-xl transition"
          >
          ×
        </span>
      </button>

    </div>

  </div>
</template>