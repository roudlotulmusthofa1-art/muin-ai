import { ref, computed } from 'vue'
import { dataRiwayat } from '../data/dataRiwayat'
import { jawabanDemo } from '../data/dataJawaban'

// =====================================================================
// "Otak" halaman Ekspor.
// State ditaruh DI DALAM fungsi (bukan di luar seperti useSesiChat),
// karena pilihan ekspor cukup hidup selama halaman Ekspor dibuka saja.
// =====================================================================

// Hanya hasil yang sudah selesai yang bisa diekspor
const pilihanHasil = dataRiwayat.filter((item) => item.status === 'selesai')

// Menyusun isi berkas Markdown dari satu hasil (data demo)
function isiMarkdown(item) {
  const temuan = jawabanDemo.temuan.map((t) => `- ${t.teks} [${t.sitasiId}]`).join('\n')
  return [
    `# ${item.judul}`,
    '',
    '> Label AI · Data demonstrasi · Bukan rujukan ilmiah',
    '',
    `**Pertanyaan:** ${item.pertanyaan}`,
    `**Cakupan:** ${item.cakupan}`,
    '**Status:** Selesai',
    '',
    '## Ringkasan',
    jawabanDemo.ringkasan,
    '',
    '## Temuan dan sitasi',
    temuan,
    '',
    '## Keterbatasan',
    jawabanDemo.keterbatasan,
    '',
  ].join('\n')
}

// Membuat berkas di browser lalu mengunduhnya (tanpa server)
function unduhBerkas(namaBerkas, isi) {
  const berkas = new Blob([isi], { type: 'text/markdown;charset=utf-8' })
  const alamat = URL.createObjectURL(berkas)
  const tautan = document.createElement('a')
  tautan.href = alamat
  tautan.download = namaBerkas
  tautan.click()
  URL.revokeObjectURL(alamat)
}

export function useEkspor() {
  // Awalnya hasil pertama sudah dicentang (seperti di desain)
  const hasilDipilih = ref([pilihanHasil[0].id])
  const format = ref('pdf')
  const pesan = ref('') // pesan setelah tombol "Buat ekspor demo" diklik

  const bisaBuat = computed(() => hasilDipilih.value.length > 0)

  function buatEkspor() {
    if (!bisaBuat.value) return
    const dipilih = pilihanHasil.filter((item) => hasilDipilih.value.includes(item.id))

    if (format.value === 'markdown') {
      const isi = dipilih.map(isiMarkdown).join('\n---\n\n')
      unduhBerkas('muin-ekspor-demo.md', isi)
      pesan.value = `Berkas Markdown dibuat dari ${dipilih.length} hasil dan diunduh.`
    } else {
      // Membuat PDF sungguhan butuh server/library tambahan, jadi di prototipe cukup simulasi
      pesan.value = `PDF demo untuk ${dipilih.length} hasil disiapkan (simulasi, belum ada berkas sungguhan).`
    }
  }

  return { pilihanHasil, hasilDipilih, format, pesan, bisaBuat, buatEkspor }
}
