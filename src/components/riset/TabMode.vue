<!-- 4 tab mode: Otomatis · Pilih Sumber · Studi Satu Kitab · Semua Kitab -->
<script setup>
import { DAFTAR_MODE } from '../../composables/useRiset'

defineProps({
  modelValue: { type: String, required: true },
})

const emit = defineEmits(['update:modelValue'])
</script>

<template>
  <div class="grid grid-cols-2 gap-2 sm:grid-cols-4" role="tablist" aria-label="Mode riset">
    <button
      v-for="mode in DAFTAR_MODE"
      :key="mode.id"
      type="button"
      role="tab"
      :aria-selected="modelValue === mode.id"
      class="h-11 rounded-xl border px-2 text-xs font-semibold transition"
      :class="
        modelValue === mode.id
          ? 'border-hijau bg-hijau-muda text-navy shadow-[inset_0_-3px_0_var(--color-hijau)]'
          : 'border-garis bg-krem-muda text-ink-soft hover:bg-white'
      "
      @click="emit('update:modelValue', mode.id)"
    >
      {{ mode.label }}
    </button>
  </div>
</template>
