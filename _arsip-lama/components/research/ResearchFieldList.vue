<script setup>
import ResearchFieldItem from './ResearchFieldItem.vue'

defineProps({
  fields: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(['toggle'])

function toggleField(field) {
  emit('toggle', field)
}
</script>

<template>
  <div class="mt-3 space-y-2">

    <ResearchFieldItem
      v-for="field in fields"
      :key="field.name"
      :field="field"
      @toggle="toggleField"
    />

  </div>
</template>