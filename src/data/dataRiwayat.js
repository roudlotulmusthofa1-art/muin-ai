// Data dummy untuk halaman "Riwayat 3 Hari" dan pilihan di halaman "Ekspor".
// sisa   : teks di kanan kartu (sisa waktu sebelum terhapus)
// nada   : warna teks "sisa" → 'aman' (hijau) | 'segera' (cokelat) | 'aktif' (hijau tua)
// status : 'selesai' (bisa diekspor) | 'berjalan' (riset belum selesai)
export const dataRiwayat = [
  {
    id: 'redaksi-syarat-akad',
    judul: 'Perbandingan redaksi syarat dalam akad',
    keterangan: 'Fikih · Syafi’i · Riset Masalah · 6 kitab demo',
    sisa: '2 hari 18 jam',
    nada: 'aman',
    status: 'selesai',
    pertanyaan:
      'Bagaimana cara membandingkan redaksi tentang syarat dalam akad dari 6 kitab Syafi’iyyah yang saya pilih?',
    cakupan: 'Fikih · Syafi’i · Riset Masalah',
  },
  {
    id: 'ibarah-thaharah',
    judul: 'Penjelasan ibarah pada bab thaharah',
    keterangan: 'Fikih · Syafi’i · Jelaskan Ibarah · Studi Satu Kitab',
    sisa: '18 jam · segera ekspor',
    nada: 'segera',
    status: 'selesai',
    pertanyaan: 'Jelaskan maksud ibarah pada bab thaharah ini.',
    cakupan: 'Fikih · Syafi’i · Jelaskan Ibarah',
  },
  {
    id: 'urutan-sumber',
    judul: 'Riset lanjutan tentang urutan sumber',
    keterangan: 'Riset berjalan · batas pekerjaan 6 hari lagi',
    sisa: 'Pekerjaan aktif',
    nada: 'aktif',
    status: 'berjalan',
    pertanyaan: 'Bagaimana urutan sumber yang dipakai dalam riset sebelumnya?',
    cakupan: 'Fikih · Syafi’i · Riset Masalah',
  },
]
