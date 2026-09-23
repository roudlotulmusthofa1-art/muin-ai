<script setup>
defineProps({
  modelValue: {
    type: String,
    required: true
  }
})

const emit = defineEmits(['update:modelValue'])

const tabs = [
  {
    value: 'otomatis',
    label: 'Otomatis'
  },
  {
    value: 'pilih',
    label: 'Pilih Sumber'
  },
  {
    value: 'satu',
    label: 'Studi Satu Kitab'
  },
  {
    value: 'semua',
    label: 'Semua Kitab'
  }
]

function selectTab(value) {
  emit('update:modelValue', value)
}
</script>

<template>
  <div class="grid grid-cols-4 gap-2">

    <button
      v-for="tab in tabs"
      :key="tab.value"
      type="button"
      class="h-11 rounded-xl border
             text-[12px] font-semibold transition"
      :class="
        modelValue === tab.value
          ? 'bg-[#edf6f2] border-[#0c8066] text-[#172c46] shadow-[inset_0_-3px_0_#087f65]'
          : 'bg-[#faf7f0] border-[#ddd5c8] text-[#666b67]'
      "
      @click="selectTab(tab.value)"
    >
      {{ tab.label }}
    </button>

  </div>
</template>