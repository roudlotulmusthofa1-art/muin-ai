<script setup>
defineProps({
  modelValue: {
    type: Boolean,
    required: true
  }
})

const emit = defineEmits(['update:modelValue'])

function updateValue(event) {
  emit('update:modelValue', event.target.checked)
}
</script>

<template>
  <label
    class="mt-3 block
           rounded-xl
           border border-[#ddd5c8]
           bg-[#fffdfa]
           p-4
           cursor-pointer
           hover:bg-[#faf8f3]
           transition"
  >

    <div class="flex items-start gap-3">

      <input
        type="checkbox"
        :checked="modelValue"
        class="mt-1 w-4 h-4 accent-[#087f65]"
        @change="updateValue"
      />

      <div>

        <p
          class="text-[15px]
                 font-bold
                 text-[#172c46]"
        >
          Hanya sumber yang saya pilih
        </p>

        <p
          class="mt-1
                 text-[12px]
                 leading-5
                 text-[#72766f]"
        >
          Jika pilihan tidak cukup, Muin menahan kesimpulan.
          Matikan untuk mengizinkan sumber pendukung wajib
          yang dilabeli terpisah.
        </p>

      </div>

    </div>

  </label>
</template>