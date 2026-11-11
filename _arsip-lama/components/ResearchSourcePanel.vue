<script setup>
import { ref } from 'vue'

import ResearchHeader from './research/ResearchHeader.vue'
import ResearchMainTabs from './research/ResearchMainTabs.vue'
import ResearchSourceTabs from './research/ResearchSourceTabs.vue'
import ResearchFilter from './research/ResearchFilter.vue'
import ResearchSourceContent from './research/ResearchSourceContent.vue'
import ResearchFooter from './research/ResearchFooter.vue'

import { researchFields as initialResearchFields } from '../data/researchFields'
import { researchAuthors as initialResearchAuthors } from '../data/researchAuthors.js'
import { researchBooks as initialResearchBooks } from '../data/researchBooks'

const emit = defineEmits(['close'])

const activeTab = ref('otomatis')
const activeSourceTab = ref('bidang')
const onlySelected = ref(false)

const researchFields = ref(
  initialResearchFields.map(field => ({ ...field }))
)

const researchAuthors = ref(
  initialResearchAuthors.map(author => ({
    ...author,
    kitabs: author.kitabs.map(kitab => ({ ...kitab }))
  }))
)

const researchBooks = ref(
  initialResearchBooks.map(book => ({ ...book }))
)

function toggleField(field) {
  field.open = !field.open
}

function toggleAuthor(author) {
  author.open = !author.open
}

function toggleKitab(author, kitab) {
  kitab.selected = !kitab.selected
}

function toggleAllAuthorKitab(author) {
  const allSelected = author.kitabs.every(k => k.selected)
  author.kitabs.forEach(k => { k.selected = !allSelected })
}

function toggleBook(book) {
  book.selected = !book.selected
}

function closeMenu() {
  emit('close')
}
</script>

<template>
  <!-- BACKDROP -->
  <div
    class="fixed inset-0 z-100 bg-slate-900/40 backdrop-blur-[2px]"
    @click.self="closeMenu"
  >

    <!-- PANEL -->
    <aside
      class="absolute right-0 top-16 bottom-1
             w-full max-w-155
             bg-[#fdfbf7]
             rounded-tl-[22px]
             rounded-bl-[22px]
             overflow-hidden
             flex flex-col
             shadow-2xl"
    >

      <!-- HEADER -->
      <ResearchHeader
        @close="closeMenu"
      />

      <!-- CONTENT -->
      <div class="flex-1 overflow-y-auto px-5 py-3">

        <!-- TAB UTAMA -->
        <ResearchMainTabs
          v-model="activeTab"
        />

        <!-- INFO OTOMATIS -->
        <div
          v-if="activeTab === 'otomatis'"
          class="mt-3 rounded-xl
                 border border-[#b9d8cf]
                 bg-[#f0f5f0]
                 px-4 py-3"
        >
          <p class="text-[13px] font-bold text-[#08745e]">
            Pencarian terstruktur, bukan acak.
          </p>

          <p class="mt-1 text-[12px] leading-5 text-[#70756f]">
            Muin tidak berhenti pada kitab yang paling dulu cocok.
            Sumber disusun menurut bidang, mazhab, peran kitab,
            dan kebijakan ilmiah domain, lalu diperiksa silang.
          </p>
        </div>

        <!-- TAB SUMBER -->
        <ResearchSourceTabs
          v-model="activeSourceTab"
        />

        <!-- FILTER -->
        <ResearchFilter
          v-model="onlySelected"
        />

        <!-- KONTEN SUMBER: berganti sesuai tab bidang / mu'allif / kitab -->
        <ResearchSourceContent
          :source-tab="activeSourceTab"
          :only-selected="onlySelected"
          :fields="researchFields"
          :authors="researchAuthors"
          :books="researchBooks"
          @toggle-field="toggleField"
          @toggle-author="toggleAuthor"
          @toggle-kitab="toggleKitab"
          @toggle-all-author-kitab="toggleAllAuthorKitab"
          @toggle-book="toggleBook"
        />

      </div>

      <!-- FOOTER -->
      <ResearchFooter
        @close="closeMenu"
      />

    </aside>
  </div>
</template>
