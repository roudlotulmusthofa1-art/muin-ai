import { ref, computed } from 'vue'
import { dataKitab, judulKitab } from '../data/dataKitab'
import { JUMLAH_BELUM_TERSEDIA } from '../data/dataBidang'

export const DAFTAR_MODE = [
  { id: 'otomatis', label: 'Otomatis' },
  { id: 'pilih-sumber', label: 'Pilih Sumber' },
  { id: 'satu-kitab', label: 'Studi Satu Kitab' },
  { id: 'semua-kitab', label: 'Semua Kitab' },
]

const SEMUA_ID = dataKitab.map((k) => k.id)

function salin(riset) {
  return { ...riset, kitabTerpilih: [...riset.kitabTerpilih] }
}

// State disimpan DI LUAR fungsi useRiset(), supaya:
// 1. semua komponen (TombolRiset, ModalRiset, daftar-daftar) berbagi data yang sama
// 2. pilihan tidak hilang saat modal ditutup

// Pilihan yang sedang dipakai (setelah klik "Gunakan pilihan")
const risetAktif = ref({
  mode: 'otomatis',
  kitabTerpilih: dataKitab.filter((k) => k.terpilihAwal).map((k) => k.id),
  kitabTunggal: dataKitab[0].id, // dipakai di mode "Studi Satu Kitab"
  hanyaPilihan: false,
})

// Salinan sementara yang diedit di dalam modal
const draf = ref(salin(risetAktif.value))

const modalTerbuka = ref(false)

// Kitab mana yang tercentang, tergantung mode
function idTerpilihDari(riset) {
  if (riset.mode === 'semua-kitab') return SEMUA_ID
  if (riset.mode === 'satu-kitab') return [riset.kitabTunggal]
  return riset.kitabTerpilih
}

export function useRiset() {
  const idTerpilih = computed(() => idTerpilihDari(draf.value))

  // Otomatis & Semua Kitab: daftar hanya untuk dilihat
  const bisaDiubah = computed(() => ['pilih-sumber', 'satu-kitab'].includes(draf.value.mode))
  // Studi Satu Kitab: centang berubah jadi radio (pilih satu)
  const modeRadio = computed(() => draf.value.mode === 'satu-kitab')
  // Centang grup (pilih semua kitab satu bidang/mu'allif) hanya di Pilih Sumber
  const bisaPilihGrup = computed(() => draf.value.mode === 'pilih-sumber')

  function apakahTerpilih(id) {
    return idTerpilih.value.includes(id)
  }

  function hitungTerpilih(ids) {
    return ids.filter(apakahTerpilih).length
  }

  // Keadaan centang grup: 'kosong', 'sebagian' (tanda −), atau 'penuh' (tanda ✓)
  function keadaanGrup(ids) {
    const jumlah = hitungTerpilih(ids)
    if (jumlah === 0) return 'kosong'
    if (jumlah === ids.length) return 'penuh'
    return 'sebagian'
  }

  function ubahKitab(id) {
    if (!bisaDiubah.value) return
    if (modeRadio.value) {
      draf.value.kitabTunggal = id
      return
    }
    const daftar = draf.value.kitabTerpilih
    draf.value.kitabTerpilih = daftar.includes(id)
      ? daftar.filter((x) => x !== id)
      : [...daftar, id]
  }

  // Klik centang grup: kalau semua sudah terpilih → kosongkan, kalau belum → pilih semua
  function ubahGrup(ids) {
    if (!bisaPilihGrup.value) return
    const semuaTerpilih = ids.every(apakahTerpilih)
    const sisa = draf.value.kitabTerpilih.filter((id) => !ids.includes(id))
    draf.value.kitabTerpilih = semuaTerpilih ? sisa : [...sisa, ...ids]
  }

  function gantiMode(mode) {
    draf.value.mode = mode
  }

  function bukaModal() {
    draf.value = salin(risetAktif.value)
    modalTerbuka.value = true
  }

  // Tutup tanpa menyimpan (draf dibuang)
  function tutupModal() {
    modalTerbuka.value = false
  }

  function gunakanPilihan() {
    risetAktif.value = salin(draf.value)
    modalTerbuka.value = false
  }

  // Teks di kaki modal (berdasarkan draf)
  const ringkasan = computed(() => {
    const total = SEMUA_ID.length
    const jumlah = idTerpilih.value.length
    const sumberLain = `${JUMLAH_BELUM_TERSEDIA} sumber lain belum tersedia`

    switch (draf.value.mode) {
      case 'pilih-sumber':
        return {
          judul: `Fokus ${jumlah} Kitab · ${total - jumlah} dikecualikan`,
          keterangan: sumberLain,
        }
      case 'satu-kitab':
        return {
          judul: `Studi Satu Kitab · ${judulKitab(draf.value.kitabTunggal)}`,
          keterangan: 'Hanya satu kitab eligible digunakan',
        }
      case 'semua-kitab':
        return { judul: `Semua Kitab · ${total} eligible`, keterangan: sumberLain }
      default:
        return {
          judul: 'Otomatis · Muin memilih sumber relevan',
          keterangan: 'Bukan hasil pertama; daftar akhir sumber tetap dapat diperiksa',
        }
    }
  })

  // Teks di tombol riset di atas kolom tanya (berdasarkan pilihan yang dipakai)
  const labelTombol = computed(() => {
    const riset = risetAktif.value
    switch (riset.mode) {
      case 'pilih-sumber':
        return `Pilih Sumber · ${riset.kitabTerpilih.length} kitab`
      case 'satu-kitab':
        return `Studi Satu Kitab · ${judulKitab(riset.kitabTunggal).replace('[Demo] ', '')}`
      case 'semua-kitab':
        return `Semua Kitab · ${SEMUA_ID.length} kitab`
      default:
        return 'Otomatis'
    }
  })

  // jumlah kitab pada pilihan yang sedang dipakai (untuk halaman chat)
  const jumlahKitabAktif = computed(() => idTerpilihDari(risetAktif.value).length)


  return {
    draf,
    risetAktif,
    modalTerbuka,
    bisaDiubah,
    modeRadio,
    bisaPilihGrup,
    apakahTerpilih,
    hitungTerpilih,
    keadaanGrup,
    ubahKitab,
    ubahGrup,
    gantiMode,
    bukaModal,
    tutupModal,
    gunakanPilihan,
    ringkasan,
    labelTombol,
    jumlahKitabAktif,
  }
}
