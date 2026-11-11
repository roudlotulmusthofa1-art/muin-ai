<!-- Centang "Hanya sumber yang saya pilih" (pakai v-model) -->
<script setup>
defineProps({
  modelValue: { type: Boolean, required: true },
})

const emit = defineEmits(['update:modelValue'])
</script>

<template>
  <label class="block cursor-pointer rounded-xl border border-garis bg-white p-4 transition hover:bg-krem-muda">
    <div class="flex items-start gap-3">
      <input
        type="checkbox"
        :checked="modelValue"
        class="mt-1 h-4 w-4 accent-hijau"
        @change="emit('update:modelValue', $event.target.checked)"
      />
      <div>
        <p class="text-[15px] font-bold text-navy">Hanya sumber yang saya pilih</p>
        <p class="mt-1 text-xs leading-5 text-ink-soft">
          Jika pilihan tidak cukup, Muin menahan kesimpulan. Matikan untuk mengizinkan sumber pendukung wajib
          yang dilabeli terpisah.
        </p>
      </div>
    </div>
  </label>
</template>
