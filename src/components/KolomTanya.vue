<script setup>
import { ref } from 'vue'

defineProps({
  modelValue: { type: String, default: '' },
  disabled: { type: Boolean, default: false },
  loading: { type: Boolean, default: false },
  placeholder: { type: String, default: 'Tanyakan kepada Muin...' },
})
const emit = defineEmits(['update:modelValue', 'submit', 'attach'])

const textarea = ref(null)

function onInput(e) {
  emit('update:modelValue', e.target.value)
  // auto-grow tinggi textarea
  e.target.style.height = 'auto'
  e.target.style.height = `${Math.min(e.target.scrollHeight, 180)}px`
}

function onKeydown(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    emit('submit')
  }
}

defineExpose({ focus: () => textarea.value?.focus() })
</script>

<template>
  <form class="w-full max-w-3xl" @submit.prevent="emit('submit')">
    <div class="flex items-end gap-3 rounded-4xl bg-white border border-black/5 shadow-input px-4 py-2.5">
      <button
        type="button"
        class="shrink-0 w-9 h-9 mb-0.5 flex items-center justify-center rounded-full text-ink-soft hover:bg-cream transition"
        aria-label="Lampirkan"
        @click="emit('attach')"
      >
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round">
          <path d="M12 5v14M5 12h14" />
        </svg>
      </button>

      <textarea
        ref="textarea"
        :value="modelValue"
        :placeholder="placeholder"
        rows="1"
        class="flex-1 resize-none bg-transparent py-2.5 text-[17px] text-ink placeholder:text-ink-faint focus:outline-none leading-6"
        @input="onInput"
        @keydown="onKeydown"
      />

      <button
        type="submit"
        :disabled="disabled"
        class="shrink-0 w-11 h-11 flex items-center justify-center rounded-full bg-navy text-white transition hover:bg-navy-dark disabled:opacity-60 disabled:cursor-not-allowed"
        aria-label="Kirim"
      >
        <svg v-if="!loading" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 19V5M5 12l7-7 7 7" />
        </svg>
        <svg v-else class="animate-spin" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
          <circle cx="12" cy="12" r="9" class="opacity-25" />
          <path d="M21 12a9 9 0 0 0-9-9" />
        </svg>
      </button>
    </div>

    <p class="mt-3 text-center text-[11px] text-ink-faint">
      Satu pertanyaan dalam satu waktu · jawaban disertai ibarah dan sitasi
    </p>
  </form>
</template>
