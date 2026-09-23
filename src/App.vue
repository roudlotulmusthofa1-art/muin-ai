<script setup>
import { ref } from 'vue'
import PrototypeBanner from './components/PrototypeBanner.vue'
import TopBar from './components/TopBar.vue'
import BrandHero from './components/BrandHero.vue'
import SuggestionChips from './components/SuggestionChips.vue'
import OptionDropdown from './components/OptionDropdown.vue'
import ChatInput from './components/ChatInput.vue'
import { useChat } from './composables/useChat'
import ResearchSourcePanel from './components/ResearchSourcePanel.vue'



const {
  question,
  scope,
  source,
  isSubmitting,
  lastSubmitted,
  canSubmit,
  applySuggestion,
  submit,
  SCOPE_OPTIONS,
  SOURCE_OPTIONS,
  SUGGESTIONS,
} = useChat()

const showResearchMenu = ref(false)

const chatInput = ref(null)

function onSuggestion(text) {
  applySuggestion(text)
  chatInput.value?.focus()
}
function toggleResearchMenu() {
  showResearchMenu.value = !showResearchMenu.value
}

function closeResearchMenu() {
  showResearchMenu.value = false
}
</script>

<template>
  <div class="min-h-screen flex flex-col bg-[#F7F2E8]">
    <PrototypeBanner />

    <TopBar
  @toggle-research-menu="toggleResearchMenu"
/>

    <main class="flex-1 flex flex-col items-center justify-center px-4 pb-20">
      <BrandHero />

      <div class="mt-14 flex flex-col items-center gap-3.5 w-full">
        <SuggestionChips :items="SUGGESTIONS" @select="onSuggestion" />

        <div class="flex flex-wrap justify-center gap-2.5">
          <OptionDropdown v-model="scope" :options="SCOPE_OPTIONS" />
          <OptionDropdown v-model="source" :options="SOURCE_OPTIONS" accent>
            <template #icon>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z" />
                <path d="M4 20.5V5.5M20 18v3H6.5" />
              </svg>
            </template>
          </OptionDropdown>
        </div>

        <div class="mt-1.5 w-full flex justify-center">
          <ChatInput
            ref="chatInput"
            v-model="question"
            :disabled="!canSubmit"
            :loading="isSubmitting"
            @submit="submit"
          />
        </div>

        <p v-if="lastSubmitted" class="mt-4 text-xs text-ink-soft">
          Pertanyaan terkirim: "{{ lastSubmitted.question }}"
        </p>
      </div>
    </main>
<ResearchSourcePanel
  v-if="showResearchMenu"
  @close="closeResearchMenu"
/>
    <footer class="px-4 pb-4 flex justify-end">
      <span class="px-3 py-1 rounded-full border border-black/10 text-[10px] font-semibold uppercase tracking-wider text-ink-faint bg-white/60">
        Prototipe UI v0.3 · Data Sintetis
      </span>
    </footer>
  </div>
</template>
