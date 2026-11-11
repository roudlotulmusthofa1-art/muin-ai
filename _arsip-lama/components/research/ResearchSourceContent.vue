<script setup>
import ResearchFieldList from './ResearchFieldList.vue'
import ResearchAuthorList from './ResearchAuthorList.vue'
import ResearchBookList from './ResearchBookList.vue'

const props = defineProps({
  sourceTab: {
    type: String,
    required: true // 'bidang' | 'muallif' | 'kitab'
  },
  onlySelected: {
    type: Boolean,
    default: false
  },
  fields: {
    type: Array,
    required: true
  },
  authors: {
    type: Array,
    required: true
  },
  books: {
    type: Array,
    required: true
  }
})

const emit = defineEmits([
  'toggle-field',
  'toggle-author',
  'toggle-kitab',
  'toggle-all-author-kitab',
  'toggle-book'
])

const infoText = {
  bidang: {
    title: 'Mulai dari bidang/fann.',
    body: 'Memilih satu blok memilih seluruh kitab eligible di bawahnya. Anda tetap dapat mengecualikan kitab tertentu.'
  },
  muallif: {
    title: "Telusuri berdasarkan mu'allif.",
    body: "Pilih seorang penulis untuk melihat seluruh kitab karyanya. Anda bisa memilih semua karyanya sekaligus, atau hanya kitab tertentu saja."
  },
  kitab: {
    title: 'Cari kitab secara langsung.',
    body: 'Gunakan pencarian untuk menemukan kitab berdasarkan judul atau nama pengarang, lalu pilih satu per satu.'
  }
}
</script>

<template>
  <div>

    <!-- INFO KONTEKSTUAL PER TAB SUMBER -->
    <div class="mt-3 rounded-xl border border-[#ddd5c8] bg-[#faf8f3] px-4 py-3">
      <p class="text-[12px] leading-5 text-[#6d716b]">
        <strong class="text-[#656a64]">{{ infoText[sourceTab].title }}</strong>
        {{ infoText[sourceTab].body }}
      </p>
    </div>

    <!-- BIDANG & MAZHAB -->
    <ResearchFieldList
      v-if="sourceTab === 'bidang'"
      :fields="fields"
      @toggle="field => emit('toggle-field', field)"
    />

    <!-- MU'ALLIF -->
    <ResearchAuthorList
      v-else-if="sourceTab === 'muallif'"
      :authors="authors"
      :only-selected="onlySelected"
      @toggle="author => emit('toggle-author', author)"
      @toggle-kitab="(author, kitab) => emit('toggle-kitab', author, kitab)"
      @toggle-all="author => emit('toggle-all-author-kitab', author)"
    />

    <!-- KITAB -->
    <ResearchBookList
      v-else-if="sourceTab === 'kitab'"
      :books="books"
      :only-selected="onlySelected"
      @toggle="book => emit('toggle-book', book)"
    />

  </div>
</template>
