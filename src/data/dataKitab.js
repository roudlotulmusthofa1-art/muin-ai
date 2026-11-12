// Data dummy kitab. INI SATU-SATUNYA daftar kitab.
// Tab Bidang, Mu'allif, dan Kitab semuanya membaca dari sini,
// jadi centang di satu tab otomatis terlihat di tab lain.
// terpilihAwal: apakah kitab tercentang saat aplikasi pertama dibuka.
export const dataKitab = [
  { id: 'mukhtasar-tajribi', judul: '[Demo] al-Mukhtasar al-Tajribi', muallifId: 'qadim', bidangId: 'fikih-syafii', label: 'Eligible demo', terpilihAwal: true },
  { id: 'masail-ikhtibar', judul: '[Demo] Masa’il al-Ikhtibar', muallifId: 'qadim', bidangId: 'fikih-syafii', label: 'Eligible demo', terpilihAwal: true },
  { id: 'bayan-iftiradi', judul: '[Demo] al-Bayan al-Iftiradi', muallifId: 'wasit', bidangId: 'fikih-syafii', label: 'Eligible demo', terpilihAwal: true },
  { id: 'tartib-namudhaji', judul: '[Demo] al-Tartib al-Namudhaji', muallifId: 'wasit', bidangId: 'fikih-syafii', label: 'Eligible demo', terpilihAwal: false },
  { id: 'sharh-masalah', judul: '[Demo] Sharh al-Mas’alah', muallifId: 'mutaakhkhir', bidangId: 'fikih-syafii', label: 'Eligible demo', terpilihAwal: true },
  { id: 'jam-nusus', judul: '[Demo] Jam’ al-Nusus', muallifId: 'mutaakhkhir', bidangId: 'fikih-syafii', label: 'Eligible demo', terpilihAwal: true },
  { id: 'hasyiyah-rabi', judul: '[Demo] Hasyiyah al-Rabi’', muallifId: 'rabi', bidangId: 'fikih-syafii', label: 'Eligible demo', terpilihAwal: false },
  { id: 'fiqh-muashir', judul: '[Demo] al-Fiqh al-Mu’ashir', muallifId: 'kontemporer', bidangId: 'fikih-syafii', label: 'Eligible demo', terpilihAwal: true },
]

export function judulKitab(id) {
  return dataKitab.find((k) => k.id === id)?.judul ?? ''
}
