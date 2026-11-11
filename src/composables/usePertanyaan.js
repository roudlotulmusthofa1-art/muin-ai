import { ref, computed } from 'vue'

export const SCOPE_OPTIONS = [
  { id: 'fikih-syafii-riset', label: 'Fikih · Syafi’i · Riset Masalah' },
  { id: 'fikih-syafii-ibarah', label: 'Fikih · Syafi’i · Jelaskan Ibarah' },
  { id: 'ushul-fikih', label: 'Ushul Fikih · Perbandingan' },
  { id: 'tafsir', label: 'Tafsir · Riset Ayat' },
]

export const SOURCE_OPTIONS = [
  { id: 'auto', label: 'Otomatis' },
  { id: 'mutun', label: 'Mutun & Syarah' },
  { id: 'fatawa', label: 'Kumpulan Fatwa' },
  { id: 'kontemporer', label: 'Kajian Kontemporer' },
]

export const SUGGESTIONS = [
  'Jelaskan ibarah Arab ini',
  'Bandingkan pendapat mu’allif',
  'Telusuri perkembangan masalah',
]

/**
 * State komposisi untuk kotak tanya Muin.
 * Semua state bersifat lokal (prototipe, data sintetis).
 */
export function useChat() {
  const question = ref('')
  const scope = ref(SCOPE_OPTIONS[0])
  const source = ref(SOURCE_OPTIONS[0])
  const isSubmitting = ref(false)
  const lastSubmitted = ref(null)

  const canSubmit = computed(() => question.value.trim().length > 0 && !isSubmitting.value)

  function applySuggestion(text) {
    question.value = text
  }

  async function submit() {
    if (!canSubmit.value) return
    isSubmitting.value = true
    try {
      // Tempat memanggil API sebenarnya. Untuk prototipe cukup simulasi.
      await new Promise((r) => setTimeout(r, 600))
      lastSubmitted.value = {
        question: question.value.trim(),
        scope: scope.value.id,
        source: source.value.id,
        at: new Date(),
      }
      question.value = ''
    } finally {
      isSubmitting.value = false
    }
  }

  return {
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
  }
}
