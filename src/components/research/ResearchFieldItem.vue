<script setup>
defineProps({
  field: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['toggle'])

function toggle() {
  emit('toggle')
}
</script>

<template>
  <div
    class="rounded-xl
           border border-[#ddd5c8]
           bg-white
           overflow-hidden"
  >

    <!-- HEADER FIELD -->
    <button
      type="button"
      class="w-full
             px-3 py-3
             flex items-center gap-3
             text-left
             hover:bg-[#fcfaf6]
             transition"
      @click="toggle"
    >

      <!-- ICON -->
      <span
        class="w-5 h-5
               rounded
               flex items-center
               justify-center
               shrink-0"
        :class="
          field.status === 'active'
            ? 'bg-[#087f65] text-white'
            : field.status === 'warning'
              ? 'text-[#172c46]'
              : 'border border-[#172c46]'
        "
      >

        <span
          v-if="field.status === 'active'"
          class="text-sm leading-none"
        >
          −
        </span>

        <span
          v-else-if="field.status === 'warning'"
          class="text-sm leading-none"
        >
          —
        </span>

      </span>

      <!-- TEXT -->
      <div class="flex-1 min-w-0">

        <p
          class="text-[15px]
                 font-bold
                 text-[#172c46]"
        >
          {{ field.name }}
        </p>

        <p
          class="text-[12px]
                 text-[#73776f]"
        >
          {{ field.description }}
        </p>

      </div>

      <!-- JUMLAH -->
      <div class="text-right shrink-0">

        <p
          class="text-[11px]
                 font-semibold"
          :class="
            field.status === 'warning'
              ? 'text-[#a36a19]'
              : 'text-[#70756f]'
          "
        >
          {{ field.books }}
        </p>

      </div>

      <span class="text-[#087f65] text-lg">
        ›
      </span>

    </button>

    <!-- DETAIL -->
    <div
      v-if="field.open && field.status === 'active'"
      class="px-12 pb-3 space-y-1"
    >

      <div class="text-[12px] text-[#73776f] py-1">
        ☑ Kitab contoh 1
      </div>

      <div class="text-[12px] text-[#73776f] py-1">
        ☑ Kitab contoh 2
      </div>

    </div>

  </div>
</template>