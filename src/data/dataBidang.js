// Data dummy bidang/fann untuk tab "Bidang & Mazhab".
// status: 'aktif' (bisa dipilih), 'nonaktif' (tampil saja), 'belum-tersedia' (label oranye)
export const dataBidang = [
  {
    id: 'fikih-syafii',
    nama: 'Fikih · Syafi’i',
    keterangan: 'Urutan mu’allif berdasarkan tahun wafat',
    status: 'aktif',
  },
  {
    id: 'fikih-hanafi',
    nama: 'Fikih · Hanafi',
    keterangan: 'Bidang tidak aktif pada chat ini',
    status: 'nonaktif',
    labelJumlah: '5 kitab demo',
  },
  {
    id: 'usul-fikih',
    nama: 'Usul Fikih',
    keterangan: 'Domain terpisah',
    status: 'nonaktif',
    labelJumlah: '6 kitab demo',
  },
  {
    id: 'sumber-tambahan',
    nama: 'Dua sumber tambahan',
    keterangan: 'Belum lolos rilis demo',
    status: 'belum-tersedia',
    labelJumlah: '2 belum tersedia',
  },
]

// Dipakai di ringkasan kaki modal: "2 sumber lain belum tersedia"
export const JUMLAH_BELUM_TERSEDIA = 2
