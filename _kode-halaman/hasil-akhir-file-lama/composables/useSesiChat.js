import { ref, computed } from 'vue'
import { LANGKAH_RISET } from '../data/dataJawaban'
import { useRiset } from './useRiset'
import router from '../router'

// =====================================================================
// "Otak" halaman chat.
// State ditaruh DI LUAR fungsi useSesiChat(), sama seperti useRiset.js,
// supaya semua komponen (sidebar, kartu, kolom chat, panel bukti)
// membaca dan mengubah data yang SAMA.
// Perpindahan halaman diurus oleh router (lihat src/router/index.js).
// =====================================================================

// Pertanyaan yang sedang diriset: { teks, cakupan, jumlahKitab }
const pertanyaanAktif = ref(null)

// Keadaan riset: 'berjalan' | 'selesai' | 'belum-cukup' | 'gangguan' | 'dibatalkan'
const status = ref('berjalan')

// Untuk kartu "Pekerjaan aktif"
const tahap = ref(0) // langkah ke berapa yang sedang berjalan (mulai dari 0)
const kitabDiperiksa = ref(0) // "4 dari 6 kitab demo telah diperiksa"

// Hasil akhir yang ingin didemokan (bisa diganti lewat PilihSkenarioDemo.vue)
const skenarioDemo = ref('selesai')

// id sitasi yang sedang dibuka di panel "Bukti dan konteks" (null = panel tertutup)
const sitasiAktif = ref(null)

// Isi kolom chat di bawah (pertanyaan lanjutan)
const teksLanjutan = ref('')

// Tombol "Aa": perbesar teks jawaban
const teksBesar = ref(false)

// ---------- Simulasi riset (pengganti backend) ----------
const JEDA_MS = 700 // jarak antar langkah, dalam milidetik
const TAHAP_PERIKSA_KITAB = 2 // langkah "Memeriksa sumber..." menghitung kitab satu per satu
let timer = null

function hentikanSimulasi() {
  clearInterval(timer)
  timer = null
}

function langkahBerikutnya() {
  // Di langkah pemeriksaan kitab: tambah 1 kitab setiap jeda
  if (
    tahap.value === TAHAP_PERIKSA_KITAB &&
    kitabDiperiksa.value < pertanyaanAktif.value.jumlahKitab
  ) {
    kitabDiperiksa.value++
    return
  }
  // Pindah ke langkah berikutnya
  if (tahap.value < LANGKAH_RISET.length - 1) {
    tahap.value++
    return
  }
  // Semua langkah selesai → tampilkan hasil sesuai skenario demo
  hentikanSimulasi()
  status.value = skenarioDemo.value
}

function jalankanSimulasi() {
  hentikanSimulasi()
  status.value = 'berjalan'
  tahap.value = 0
  kitabDiperiksa.value = 0
  sitasiAktif.value = null
  timer = setInterval(langkahBerikutnya, JEDA_MS)
}

export function useSesiChat() {
  const sedangBerjalan = computed(() => status.value === 'berjalan')

  // "Fikih · Syafi’i · Riset Masalah" → bidang: "Fikih · Syafi’i", tugas: "Riset Masalah"
  const bagianCakupan = computed(() => (pertanyaanAktif.value?.cakupan ?? '').split(' · '))
  const ringkasCakupan = computed(() => ({
    bidang: bagianCakupan.value.slice(0, -1).join(' · '),
    tugas: bagianCakupan.value.at(-1),
  }))

  // Dipanggil dari halaman beranda (kirim pertama) dan dari kolom chat (lanjutan)
  function mulaiRiset(teks, cakupan) {
    const { jumlahKitabAktif } = useRiset()
    pertanyaanAktif.value = { teks, cakupan, jumlahKitab: jumlahKitabAktif.value }
    teksLanjutan.value = ''
    jalankanSimulasi()
    // Pindah ke alamat /chat (kalau sudah di /chat, tidak terjadi apa-apa)
    router.push({ name: 'chat' })
  }

  function kirimLanjutan() {
    const teks = teksLanjutan.value.trim()
    if (!teks || sedangBerjalan.value) return
    mulaiRiset(teks, pertanyaanAktif.value.cakupan)
  }

  function batalkan() {
    hentikanSimulasi()
    status.value = 'dibatalkan'
  }

  // "Coba lagi gratis" / "Risetkan ulang gratis" / "Mulai lagi"
  // Memakai mulaiRiset lagi supaya jumlah kitab ikut diperbarui (misal setelah "Ubah sumber")
  function cobaLagi() {
    mulaiRiset(pertanyaanAktif.value.teks, pertanyaanAktif.value.cakupan)
  }

  // "Ubah pertanyaan": salin pertanyaan lama ke kolom chat supaya bisa diedit
  function ubahPertanyaan() {
    teksLanjutan.value = pertanyaanAktif.value.teks
  }

  async function chatBaru() {
    hentikanSimulasi()
    // Pindah halaman DULU, baru kosongkan data.
    // Kalau dibalik, halaman chat sempat mencoba menampilkan pertanyaan yang sudah kosong → error.
    await router.push({ name: 'beranda' })
    pertanyaanAktif.value = null
    sitasiAktif.value = null
    teksLanjutan.value = ''
  }

  // Dipanggil dari halaman Riwayat: buka lagi hasil lama di halaman chat
  function bukaRiwayat(item) {
    // Riset yang masih berjalan → jalankan lagi simulasinya
    if (item.status === 'berjalan') {
      mulaiRiset(item.pertanyaan, item.cakupan)
      return
    }
    // Riset yang sudah selesai → langsung tampilkan hasilnya
    hentikanSimulasi()
    const { jumlahKitabAktif } = useRiset()
    pertanyaanAktif.value = {
      teks: item.pertanyaan,
      cakupan: item.cakupan,
      jumlahKitab: jumlahKitabAktif.value,
    }
    status.value = 'selesai'
    sitasiAktif.value = null
    teksLanjutan.value = ''
    router.push({ name: 'chat' })
  }

  function bukaBukti(id) {
    sitasiAktif.value = id
  }

  function tutupBukti() {
    sitasiAktif.value = null
  }

  // Ganti hasil demo. Kalau riset sudah tidak berjalan, hasilnya langsung diganti.
  function pilihSkenario(id) {
    skenarioDemo.value = id
    if (!sedangBerjalan.value) {
      status.value = id
      sitasiAktif.value = null
    }
  }

  function gantiUkuranTeks() {
    teksBesar.value = !teksBesar.value
  }

  return {
    pertanyaanAktif,
    status,
    tahap,
    kitabDiperiksa,
    skenarioDemo,
    sitasiAktif,
    teksLanjutan,
    teksBesar,
    sedangBerjalan,
    ringkasCakupan,
    bagianCakupan,
    mulaiRiset,
    kirimLanjutan,
    batalkan,
    cobaLagi,
    ubahPertanyaan,
    chatBaru,
    bukaRiwayat,
    bukaBukti,
    tutupBukti,
    pilihSkenario,
    gantiUkuranTeks,
  }
}
