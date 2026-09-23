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
    value: 'bidang',
    label: 'Bidang & Mazhab'
  },
  {
    value: 'muallif',
    label: "Mu'allif"
  },
  {
    value: 'kitab',
    label: 'Kitab'
  }
]

function selectTab(value) {
  emit('update:modelValue', value)
}
</script>

<template>
  <div
    class="mt-3 flex
           rounded-xl
           bg-[#eee8dd]
           p-1"
  >

    <button
      v-for="tab in tabs"
      :key="tab.value"
      type="button"
      class="flex-1 py-2.5
             rounded-lg
             text-[12px]
             font-bold transition"
      :class="
        modelValue === tab.value
          ? 'bg-white text-[#172c46] shadow-sm'
          : 'text-[#6f736e]'
      "
      @click="selectTab(tab.value)"
    >
      {{ tab.label }}
    </button>

  </div>
</template>