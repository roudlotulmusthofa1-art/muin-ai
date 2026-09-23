<script setup>
defineProps({
  items: { type: Array, required: true },
})
const emit = defineEmits(['select'])
</script>

<template>
  <div class="flex flex-wrap justify-center gap-2.5">
    <button
      v-for="item in items"
      :key="item"
      type="button"
      class="px-4 py-2 rounded-full bg-white/80 border border-black/5 shadow-chip text-[13px] text-ink hover:bg-white hover:border-navy/20 transition"
      @click="emit('select', item)"
    >
      {{ item }}
    </button>
  </div>
</template>
