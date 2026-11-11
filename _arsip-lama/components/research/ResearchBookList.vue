<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  books: {
    type: Array,
    required: true
  },
  onlySelected: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['toggle'])

const query = ref('')

const levelColor = {
  Pemula: 'bg-[#edf6f2] text-[#08745e]',
  Menengah: 'bg-[#fbeee0] text-[#a15c1f]',
  Lanjut: 'bg-[#f3e8ec] text-[#8a2e4d]'
}

const visibleBooks = computed(() => {
  let list = props.books

  if (props.onlySelected) {
    list = list.filter(book => book.selected)
  }

  const q = query.value.trim().toLowerCase()
  if (q) {
    list = list.filter(book =>
      book.title.toLowerCase().includes(q) ||
      book.author.toLowerCase().includes(q)
    )
  }

  return list
})

function toggle(book) {
  emit('toggle', book)
}
</script>

<template>
  <div class="mt-3">

    <!-- PENCARIAN KITAB -->
    <input
      v-model="query"
      type="text"
      placeholder="Cari judul kitab atau nama pengarang..."
      class="w-full h-10 rounded-xl border border-[#ddd5c8]
             bg-[#faf8f3] px-3 mb-2
             text-[12px] text-[#4b4f47]
             placeholder:text-[#a9ada3]
             focus:outline-none focus:border-[#0c8066]"
    />

    <div class="space-y-1.5">
      <label
        v-for="book in visibleBooks"
        :key="book.id"
        class="flex items-center gap-3 rounded-xl border border-[#ddd5c8]
               bg-[#faf8f3] px-3 py-2.5 cursor-pointer"
      >
        <input
          type="checkbox"
          class="h-4 w-4 rounded border-[#c7bfaf] accent-[#08745e]"
          :checked="book.selected"
          @change="toggle(book)"
        />

        <div class="min-w-0 flex-1">
          <p class="text-[12.5px] font-semibold text-[#172c46] truncate">
            {{ book.title }}
          </p>
          <p class="text-[11px] text-[#8a8f86] truncate">
            {{ book.author }} · {{ book.bidang }}
          </p>
        </div>

        <span
          class="text-[10px] font-semibold rounded-full px-2 py-0.5 shrink-0"
          :class="levelColor[book.level] || 'bg-[#f0efe9] text-[#6d716b]'"
        >
          {{ book.level }}
        </span>
      </label>

      <p v-if="visibleBooks.length === 0" class="text-[12px] text-[#9a9e94] text-center py-6">
        Kitab tidak ditemukan.
      </p>
    </div>

  </div>
</template>
