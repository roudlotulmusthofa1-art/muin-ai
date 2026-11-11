<script setup>
import { computed } from 'vue'

const props = defineProps({
  authors: {
    type: Array,
    required: true
  },
  onlySelected: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['toggle', 'toggle-kitab', 'toggle-all'])

const visibleAuthors = computed(() =>
  props.onlySelected
    ? props.authors.filter(author => author.kitabs.some(k => k.selected))
    : props.authors
)

function selectedCount(author) {
  return author.kitabs.filter(k => k.selected).length
}

function toggleAuthor(author) {
  emit('toggle', author)
}

function toggleKitab(author, kitab) {
  emit('toggle-kitab', author, kitab)
}

function toggleAll(author) {
  emit('toggle-all', author)
}
</script>

<template>
  <div class="mt-3 space-y-2">

    <div
      v-for="author in visibleAuthors"
      :key="author.id"
      class="rounded-xl border border-[#ddd5c8] bg-[#faf8f3] overflow-hidden"
    >

      <!-- HEADER MU'ALLIF -->
      <button
        type="button"
        class="w-full flex items-center justify-between gap-3 px-4 py-3 text-left"
        @click="toggleAuthor(author)"
      >
        <div class="flex items-center gap-3 min-w-0">
          <input
            type="checkbox"
            class="h-4 w-4 rounded border-[#c7bfaf] accent-[#08745e]"
            :checked="selectedCount(author) === author.kitabs.length"
            @click.stop="toggleAll(author)"
          />
          <div class="min-w-0">
            <p class="text-[13px] font-bold text-[#172c46] truncate">
              {{ author.name }}
            </p>
            <p class="text-[11px] text-[#8a8f86] truncate">
              {{ author.era }} · {{ author.mazhab }}
            </p>
          </div>
        </div>

        <div class="flex items-center gap-2 shrink-0">
          <span class="text-[11px] font-semibold text-[#08745e] bg-[#edf6f2] rounded-full px-2 py-0.5">
            {{ selectedCount(author) }}/{{ author.kitabs.length }}
          </span>
          <svg
            class="h-4 w-4 text-[#9a9e94] transition-transform"
            :class="author.open ? 'rotate-180' : ''"
            viewBox="0 0 20 20" fill="currentColor"
          >
            <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.19l3.71-3.96a.75.75 0 111.1 1.02l-4.25 4.54a.75.75 0 01-1.1 0L5.21 8.27a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
          </svg>
        </div>
      </button>

      <!-- DAFTAR KITAB KARYA MU'ALLIF -->
      <div v-if="author.open" class="border-t border-[#ddd5c8] bg-white px-4 py-2">
        <label
          v-for="kitab in author.kitabs"
          :key="kitab.id"
          class="flex items-center gap-2 py-1.5 cursor-pointer"
        >
          <input
            type="checkbox"
            class="h-3.5 w-3.5 rounded border-[#c7bfaf] accent-[#08745e]"
            :checked="kitab.selected"
            @change="toggleKitab(author, kitab)"
          />
          <span class="text-[12px] text-[#4b4f47]">{{ kitab.title }}</span>
          <span class="ml-auto text-[10px] text-[#9a9e94]">{{ kitab.bidang }}</span>
        </label>
      </div>

    </div>

    <p v-if="visibleAuthors.length === 0" class="text-[12px] text-[#9a9e94] text-center py-6">
      Tidak ada mu'allif yang cocok dengan filter ini.
    </p>

  </div>
</template>
