import { ref, computed } from 'vue'
import { useRiset } from './useRiset'

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
  const { risetAktif } = useRiset()

  const pertanyaan = ref('')
  const cakupan = ref(PILIHAN_CAKUPAN[0])
  const sedangMengirim = ref(false)
  const terakhirDikirim = ref(null)

  const bisaKirim = computed(() => pertanyaan.value.trim().length > 0 && !sedangMengirim.value)

  function pakaiSaran(teks) {
    pertanyaan.value = teks
  }

  async function kirim() {
    if (!bisaKirim.value) return
    sedangMengirim.value = true
    try {
      // Tempat memanggil API sebenarnya. Untuk prototipe cukup simulasi.
      await new Promise((r) => setTimeout(r, 600))
      terakhirDikirim.value = {
        pertanyaan: pertanyaan.value.trim(),
        cakupan: cakupan.value.id,
        riset: { ...risetAktif.value },
        waktu: new Date(),
      }
      pertanyaan.value = ''
    } finally {
      sedangMengirim.value = false
    }
  }

  return {
    pertanyaan,
    cakupan,
    sedangMengirim,
    terakhirDikirim,
    bisaKirim,
    pakaiSaran,
    kirim,
  }
}
