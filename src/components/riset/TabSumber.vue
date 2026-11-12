<!-- 3 tab sumber: Bidang & Mazhab · Mu'allif · Kitab -->
<script setup>
defineProps({
  modelValue: { type: String, required: true },
})

const emit = defineEmits(['update:modelValue'])

const daftarTab = [
  { id: 'bidang', label: 'Bidang & Mazhab' },
  { id: 'muallif', label: 'Mu’allif' },
  { id: 'kitab', label: 'Kitab' },
]
</script>

<template>
  <div class="flex rounded-xl bg-[#eee8dd] p-1" role="tablist" aria-label="Cara memilih sumber">
    <button
      v-for="tab in daftarTab"
      :key="tab.id"
      type="button"
      role="tab"
      :aria-selected="modelValue === tab.id"
      class="flex-1 rounded-lg py-2.5 text-xs font-bold transition"
      :class="modelValue === tab.id ? 'bg-white text-navy shadow-sm' : 'text-ink-soft hover:text-navy'"
      @click="emit('update:modelValue', tab.id)"
    >
      {{ tab.label }}
    </button>
  </div>
</template>
