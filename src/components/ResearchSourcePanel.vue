<script setup>
import { ref } from 'vue'

import ResearchHeader from './research/ResearchHeader.vue'
import ResearchMainTabs from './research/ResearchMainTabs.vue'
import ResearchSourceTabs from './research/ResearchSourceTabs.vue'
import ResearchFilter from './research/ResearchFilter.vue'
import ResearchFieldList from './research/ResearchFieldList.vue'
import ResearchFooter from './research/ResearchFooter.vue'

import { researchFields as initialResearchFields } from '../data/researchFields'

const emit = defineEmits(['close'])

const activeTab = ref('otomatis')
const activeSourceTab = ref('bidang')
const onlySelected = ref(false)

const researchFields = ref(
  initialResearchFields.map(field => ({ ...field }))
)

function toggleField(field) {
  field.open = !field.open
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
          <p
            class="text-[13px]
                   font-bold
                   text-[#08745e]"
          >
            Pencarian terstruktur, bukan acak.
          </p>

          <p
            class="mt-1 text-[12px]
                   leading-5
                   text-[#70756f]"
          >
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

        <!-- INFO -->
        <div
          class="mt-3
                 rounded-xl
                 border border-[#ddd5c8]
                 bg-[#faf8f3]
                 px-4 py-3"
        >
          <p
            class="text-[12px]
                   leading-5
                   text-[#6d716b]"
          >
            <strong class="text-[#656a64]">
              Mulai dari bidang/fann.
            </strong>

            Memilih satu blok memilih seluruh kitab eligible
            di bawahnya. Anda tetap dapat mengecualikan kitab tertentu.
          </p>
        </div>

        <!-- DAFTAR BIDANG -->
        <ResearchFieldList
          :fields="researchFields"
          @toggle="toggleField"
        />

      </div>

      <!-- FOOTER -->
      <ResearchFooter
        @close="closeMenu"
      />

    </aside>
  </div>
</template>