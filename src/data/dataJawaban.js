// Data dummy untuk halaman chat.
// SEMUA ISI DI SINI SINTETIS — bukan jawaban ilmiah, hanya untuk menguji tampilan.

// Langkah-langkah yang tampil saat riset sedang berjalan (kartu "Pekerjaan aktif").
// teksMenunggu dipakai kalau langkah itu belum dimulai.
export const LANGKAH_RISET = [
  { teks: 'Konteks dan selector dikunci.' },
  { teks: 'Daftar akhir sumber diperiksa.' },
  { teks: 'Memeriksa sumber sesuai cakupan aktif.' },
  {
    teks: 'Validasi ibarah dan sitasi.',
    teksMenunggu: 'Validasi ibarah dan sitasi belum dimulai.',
  },
]

// Hasil saat riset selesai
export const jawabanDemo = {
  statistikTambahan: ['3 sumber relevan dan dikutip', 'Urutan sumber mengikuti kebijakan domain'],
  peringatan: {
    judul: 'Contoh tampilan - bukan jawaban ilmiah.',
    isi: 'Seluruh nama kitab, kutipan, sitasi, halaman, dan hasil di layar ini sintetis untuk menguji antarmuka.',
  },
  ringkasan:
    'Prototipe ini memperagakan cara Muin menetapkan ruang lingkup, mengelompokkan redaksi, mempertahankan teks Arab, menautkan temuan kepada bukti, lalu menyatakan keterbatasannya. Bagian ini sengaja tidak menetapkan hukum fikih apa pun.',
  // sitasiId harus sama dengan kunci di dataSitasi.js
  temuan: [
    {
      teks: 'Sumber pertama memuat redaksi contoh yang paling ringkas.',
      sitasiId: 'mukhtasar-2-145',
    },
    {
      teks: 'Sumber kedua menyusun syarat yang sama dengan urutan berbeda.',
      sitasiId: 'bayan-1-88',
    },
    {
      teks: 'Sumber ketiga menambahkan penjelasan, tetapi tidak mengubah redaksi inti.',
      sitasiId: 'sharh-3-212',
    },
  ],
  keterbatasan:
    'Data demo tidak memuat naskah asli, perbandingan edisi, maupun konteks halaman yang lengkap. Gunakan hanya untuk menguji tampilan.',
}

// Hasil saat bukti tidak cukup (kartu kuning)
// status: 'selesai' (✓) | 'peringatan' (!) | 'catatan' (—)  → lihat DaftarLangkah.vue
export const laporanBelumCukup = {
  label: 'Laporan riset belum cukup',
  judul: 'Kesimpulan ditahan',
  deskripsi: 'Muin belum menemukan bukti terverifikasi yang cukup untuk menjawab pertanyaan ini.',
  rincian: [
    { status: 'selesai', label: 'Yang diperiksa:', teks: '6 kitab demo pilihan pengguna.' },
    {
      status: 'selesai',
      label: 'Yang ditemukan:',
      teks: '3 redaksi sintetis untuk pengujian tampilan.',
    },
    {
      status: 'peringatan',
      label: 'Yang belum tersedia:',
      teks: 'naskah, edisi, konteks halaman, dan hubungan ilmiah nyata.',
    },
    {
      status: 'catatan',
      label: 'Alasan ditahan:',
      teks: 'data prototipe tidak dapat mendukung kesimpulan fikih.',
    },
  ],
}

// Hasil saat terjadi gangguan teknis (kartu merah)
export const laporanGangguan = {
  label: 'Gangguan teknis',
  judul: 'Pekerjaan belum dapat diselesaikan',
  deskripsi:
    'Riset sudah diterima, tetapi validator demonstrasi tidak dapat menyelesaikan pemeriksaan. Pertanyaan dan pengaturan Anda tetap tersedia.',
  kodeBantuan: 'DEMO-JOB-04',
}

// Saat pengguna menekan "Batalkan"
export const laporanDibatalkan = {
  label: 'Riset dibatalkan',
  judul: 'Pekerjaan dihentikan',
  deskripsi: 'Tidak ada hasil yang disimpan. Pertanyaan dan pengaturan Anda tetap tersedia.',
}
