<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

defineProps({
  modelValue: { type: Object, required: true },
  options: { type: Array, required: true },
  accent: { type: Boolean, default: false },
})
const emit = defineEmits(['update:modelValue'])

const open = ref(false)
const root = ref(null)

function choose(option) {
  emit('update:modelValue', option)
  open.value = false
}

function onClickOutside(e) {
  if (root.value && !root.value.contains(e.target)) open.value = false
}

onMounted(() => document.addEventListener('click', onClickOutside))
onBeforeUnmount(() => document.removeEventListener('click', onClickOutside))
</script>

<template>
  <div ref="root" class="relative">
    <button
      type="button"
      class="flex items-center gap-1.5 px-4 py-2 rounded-full bg-white border border-black/5 shadow-chip text-[13px] font-semibold transition hover:border-navy/20"
      :class="accent ? 'text-emerald-brand' : 'text-ink'"
      @click="open = !open"
    >
      <slot name="icon" />
      <span>{{ modelValue.label }}</span>
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" class="text-ink-faint">
        <path d="M6 9l6 6 6-6" />
      </svg>
    </button>

    <Transition
      enter-active-class="transition duration-100 ease-out"
      enter-from-class="opacity-0 translate-y-1"
      leave-active-class="transition duration-75 ease-in"
      leave-to-class="opacity-0 translate-y-1"
    >
      <ul
        v-if="open"
        class="absolute z-20 mt-2 min-w-[14rem] rounded-xl bg-white border border-black/5 shadow-input py-1.5 text-[13px]"
      >
        <li v-for="opt in options" :key="opt.id">
          <button
            type="button"
            class="w-full text-left px-4 py-2 hover:bg-cream transition"
            :class="opt.id === modelValue.id ? 'font-semibold text-navy' : 'text-ink'"
            @click="choose(opt)"
          >
            {{ opt.label }}
          </button>
        </li>
      </ul>
    </Transition>
  </div>
</template>
