import { ref, computed } from 'vue'
import { useSesiChat } from './useSesiChat'

export const PILIHAN_CAKUPAN = [
  { id: 'fikih-syafii-riset', label: 'Fikih · Syafi’i · Riset Masalah' },
  { id: 'fikih-syafii-ibarah', label: 'Fikih · Syafi’i · Jelaskan Ibarah' },
  { id: 'ushul-fikih', label: 'Ushul Fikih · Perbandingan' },
  { id: 'tafsir', label: 'Tafsir · Riset Ayat' },
]

export const SARAN = [
  'Jelaskan ibarah Arab ini',
  'Bandingkan pendapat mu’allif',
  'Telusuri perkembangan masalah',
]

/**
 * State untuk kotak tanya Muin.
 * Semua state bersifat lokal (prototipe, data sintetis).
 */
export function usePertanyaan() {
  const { mulaiRiset } = useSesiChat()

  const pertanyaan = ref('')
  const cakupan = ref(PILIHAN_CAKUPAN[0])


  const bisaKirim = computed(() => pertanyaan.value.trim().length > 0)

  function pakaiSaran(teks) {
    pertanyaan.value = teks
  }

  function kirim() {
    if (!bisaKirim.value) return
    mulaiRiset(pertanyaan.value.trim(), cakupan.value.label)
    pertanyaan.value = ''
  }

  return {
    pertanyaan,
    cakupan,
    bisaKirim,
    pakaiSaran,
    kirim,
  }
}
