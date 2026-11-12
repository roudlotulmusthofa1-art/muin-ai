// Data dummy sitasi (rujukan halaman kitab) untuk panel "Bukti dan konteks".
// Teks Arab di sini SINTETIS, bukan kutipan kitab sungguhan.
import { dataKitab } from './dataKitab'
import { dataMuallif } from './dataMuallif'
import { dataBidang } from './dataBidang'

const EDISI_DEMO = 'Cetakan Prototipe Sintetis, 1448 H'
const PROVENANS_DEMO = 'Fixture antarmuka; tanpa PDF atau katalog nyata'

// Kunci (contoh 'mukhtasar-2-145') = id sitasi, dipakai di dataJawaban.js
// teks dibagi 3: sebelum + sorot (diberi warna) + sesudah
export const dataSitasi = {
  'mukhtasar-2-145': {
    kitabId: 'mukhtasar-tajribi',
    jilid: 2,
    halaman: 145,
    bab: 'Bab Demo tentang Syarat',
    teks: {
      sebelum: 'هٰذَا نَصٌّ تَجْرِيبِيٌّ مُصْطَنَعٌ لِاخْتِبَارِ عَرْضِ ',
      sorot: 'الْعِبَارَةِ الْعَرَبِيَّةِ',
      sesudah:
        ' فِي الْوَاجِهَةِ، وَلَيْسَ نَقْلًا مِنْ كِتَابٍ، وَلَا دَلِيلًا عَلَى حُكْمٍ شَرْعِيٍّ.',
    },
  },
  'bayan-1-88': {
    kitabId: 'bayan-iftiradi',
    jilid: 1,
    halaman: 88,
    bab: 'Bab Demo tentang Rukun',
    teks: {
      sebelum: 'وَهٰذِهِ عِبَارَةٌ تَجْرِيبِيَّةٌ ثَانِيَةٌ تُرَتِّبُ ',
      sorot: 'الشُّرُوطَ الْمَفْرُوضَةَ',
      sesudah: ' تَرْتِيبًا مُخْتَلِفًا لِأَجْلِ اخْتِبَارِ الْمُقَارَنَةِ فِي الشَّاشَةِ فَقَطْ.',
    },
  },
  'sharh-3-212': {
    kitabId: 'sharh-masalah',
    jilid: 3,
    halaman: 212,
    bab: 'Bab Demo tentang Penjelasan',
    teks: {
      sebelum: 'وَفِي هٰذَا الشَّرْحِ الْمُفْتَرَضِ زِيَادَةُ بَيَانٍ ',
      sorot: 'لَا تُغَيِّرُ أَصْلَ الْعِبَارَةِ',
      sesudah: '، وَإِنَّمَا وُضِعَتْ لِتَجْرِبَةِ عَرْضِ الْحَوَاشِي.',
    },
  },
}

// Teks untuk halaman sebelum/sesudah halaman yang dikutip (tanpa sorotan)
const TEKS_HALAMAN_SEKITAR =
  'هٰذِهِ صَفْحَةٌ تَجْرِيبِيَّةٌ لِعَرْضِ السِّيَاقِ الْمُجَاوِرِ فَقَطْ، وَلَا تَحْتَوِي عَلَى مَوْضِعِ الِاسْتِشْهَادِ.'

// Teks yang tampil untuk nomor halaman tertentu
export function teksHalaman(sitasi, halaman) {
  if (halaman === sitasi.halaman) return sitasi.teks
  return { sebelum: TEKS_HALAMAN_SEKITAR, sorot: '', sesudah: '' }
}

// Label singkat untuk chip: "[Demo] al-Mukhtasar al-Tajribi 2/145"
export function labelSitasi(id) {
  const sitasi = dataSitasi[id]
  const kitab = dataKitab.find((k) => k.id === sitasi.kitabId)
  return `${kitab.judul} ${sitasi.jilid}/${sitasi.halaman}`
}

// Gabungkan sitasi dengan data kitab, mu'allif, dan bidang → siap ditampilkan
export function detailSitasi(id) {
  const sitasi = dataSitasi[id]
  const kitab = dataKitab.find((k) => k.id === sitasi.kitabId)
  const muallif = dataMuallif.find((m) => m.id === kitab.muallifId)
  const bidang = dataBidang.find((b) => b.id === kitab.bidangId)

  return {
    ...sitasi,
    id,
    judul: kitab.judul,
    muallif: `${muallif.nama} · ${muallif.keterangan} sintetis`,
    bidang: bidang.nama,
    edisi: EDISI_DEMO,
    lokasi: `Jilid ${sitasi.jilid} · halaman ${sitasi.halaman}`,
    provenans: PROVENANS_DEMO,
    label: labelSitasi(id),
  }
}
