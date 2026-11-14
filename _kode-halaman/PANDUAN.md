# Panduan: Halaman Riwayat 3 Hari, Ekspor, dan Akun

- **13 file BARU**: salin dari `_kode-halaman/src/` ke lokasi yang sama di `src/`.
- **3 file LAMA**: ubah per poin di bawah ini.
- **1 file DIHAPUS**: `src/halaman/HalamanSegeraHadir.vue` (sudah tidak dipakai).
- Versi jadi file lama ada di `_kode-halaman/hasil-akhir-file-lama/`. Pakai hanya untuk mencocokkan, jangan disalin.

> Selama langkah belum selesai semua, browser wajar menampilkan error.

---

## Gambaran: komponen yang dipakai bersama

Ketiga halaman punya bentuk yang sama, jadi bagian yang berulang dibuat sekali di `components/umum/`:

```
TataLetakHalaman  ← kerangka halaman
├── KepalaHalaman ← [☰] Judul · subjudul ....... [Data demonstrasi] [Aa]
├── LABEL KECIL / Judul Besar / Deskripsi
└── <slot>        ← isi khusus tiap halaman
      └── KartuBagian (kartu putih: judul + deskripsi + isi)
```

`KepalaHalaman` juga dipakai ulang oleh halaman **Chat** (lihat poin C), jadi bagian atas semua halaman sekarang seragam.

---

## Langkah 1: File BARU (13)

### Data dummy
- [ ] `src/data/dataRiwayat.js`: 3 riwayat (dipakai halaman Riwayat **dan** pilihan di Ekspor)
- [ ] `src/data/dataAkun.js`: isi kartu-kartu Akun

### Composable
- [ ] `src/composables/useEkspor.js`: logika Ekspor (pilihan, format, membuat berkas)

### Komponen umum (dipakai berulang)
- [ ] `src/components/umum/KepalaHalaman.vue`
- [ ] `src/components/umum/TataLetakHalaman.vue`
- [ ] `src/components/umum/KartuBagian.vue`

### Komponen per halaman (buat folder baru: `riwayat/`, `ekspor/`, `akun/`)
- [ ] `src/components/riwayat/KartuRiwayat.vue`
- [ ] `src/components/ekspor/PilihHasil.vue`
- [ ] `src/components/ekspor/PilihFormat.vue`
- [ ] `src/components/akun/BarisInfo.vue`

### Halaman
- [ ] `src/halaman/HalamanRiwayat.vue`
- [ ] `src/halaman/HalamanEkspor.vue`
- [ ] `src/halaman/HalamanAkun.vue`

---

## Langkah 2: Ubah file LAMA per poin

### A. `src/router/index.js` (2 poin)

**A1.** Di komentar bagian atas, ganti 2 baris ini:
```js
//   localhost:5173/riwayat   → HalamanSegeraHadir (belum dibuat)
//   ...
```
menjadi:
```js
//   localhost:5173/riwayat   → HalamanRiwayat
//   localhost:5173/ekspor    → HalamanEkspor
//   localhost:5173/akun      → HalamanAkun
```
(Ini hanya komentar, jadi tidak memengaruhi cara kerja. Tapi biasakan komentar selalu sesuai kode.)

**A2.** Ganti 3 route "Segera hadir". Hapus mulai dari komentar `// Menu sidebar yang halamannya belum dibuat ...` sampai route `/akun` selesai (`},`), lalu ketik:
```js
  {
    path: '/riwayat',
    name: 'riwayat',
    component: () => import('../halaman/HalamanRiwayat.vue'),
  },
  {
    path: '/ekspor',
    name: 'ekspor',
    component: () => import('../halaman/HalamanEkspor.vue'),
  },
  {
    path: '/akun',
    name: 'akun',
    component: () => import('../halaman/HalamanAkun.vue'),
  },
```
**Kenapa `meta: { judul }` hilang?** Dulu satu file `HalamanSegeraHadir` dipakai 3 alamat, jadi judulnya dikirim lewat `meta`.
Sekarang setiap alamat punya halaman sendiri yang sudah tahu judulnya.
**`name` tetap sama** (`riwayat`, `ekspor`, `akun`), jadi menu sidebar tidak perlu diubah.

---

### B. `src/composables/useSesiChat.js` (2 poin)

**B1.** Tambah fungsi baru **tepat di bawah** fungsi `chatBaru` (setelah `}` penutupnya):
```js
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
```

**B2.** Di dalam `return { ... }` paling bawah, di bawah baris `chatBaru,`, tambahkan:
```js
    bukaRiwayat,
```
**Kenapa?** Saat kartu riwayat diklik, pertanyaannya diisi ke `pertanyaanAktif`, lalu pindah ke `/chat`.
Karena `pertanyaanAktif` sudah terisi, "penjaga pintu" di router mengizinkan halaman chat terbuka.

---

### C. `src/components/chat/KepalaChat.vue` (2 poin, isinya jadi jauh lebih pendek)

**C1.** Ganti seluruh bagian `<script setup> ... </script>` dengan:
```vue
<script setup>
import { useSesiChat } from '../../composables/useSesiChat'
import LencanaPil from '../umum/LencanaPil.vue'
import KepalaHalaman from '../umum/KepalaHalaman.vue'

const { sedangBerjalan } = useSesiChat()
</script>
```

**C2.** Ganti seluruh bagian `<template> ... </template>` dengan:
```vue
<template>
  <!-- Memakai KepalaHalaman (sama dengan halaman lain), ditambah satu lencana khusus chat -->
  <KepalaHalaman judul="Chat" subjudul="Meja Baca Tenang">
    <span class="hidden md:block">
      <LencanaPil>
        {{ sedangBerjalan ? 'Pekerjaan aktif · hingga 7 hari' : 'Terhapus dalam 2 hari 18 jam' }}
      </LencanaPil>
    </span>
  </KepalaHalaman>
</template>
```
**Kenapa?** Tombol ☰, judul, "Data demonstrasi", dan "Aa" sekarang ada di `KepalaHalaman`.
Halaman chat hanya **menitipkan** satu lencana tambahan lewat **slot** (bagian di antara `<KepalaHalaman>` dan `</KepalaHalaman>`).
Kalau nanti tombol "Aa" mau diubah, cukup ubah satu file (`KepalaHalaman.vue`), dan semua halaman ikut berubah.

---

## Langkah 3: Hapus file yang tidak dipakai
- [ ] Hapus `src/halaman/HalamanSegeraHadir.vue`

Lakukan **setelah** poin A selesai. Kalau dihapus sebelum router diubah, router masih mencari file ini dan muncul error.

---

## Langkah 4: Coba
1. Klik menu **Riwayat 3 Hari**: muncul 3 kartu. Warna sisa waktunya hijau, cokelat, dan hijau tua.
2. Klik kartu **Perbandingan redaksi syarat dalam akad**: pindah ke chat dan hasilnya langsung tampil.
3. Klik kartu **Riset lanjutan ...**: pindah ke chat dan risetnya berjalan.
4. Klik menu **Ekspor**:
   - pilih **Markdown** → **Buat ekspor demo**: berkas `muin-ekspor-demo.md` terunduh (buka dengan editor teks);
   - pilih **PDF** → muncul pesan simulasi;
   - hapus semua centang: tombol mati dan muncul "Pilih minimal satu hasil".
5. Klik menu **Akun**: muncul 5 kartu. Klik **Keluar dari akun demo** dan pesan simulasi muncul.
6. Cek halaman **Chat**: bagian atasnya harus tetap sama seperti sebelumnya.

Setelah semua jalan: **Commit → Sync**, lalu hapus folder `_kode-halaman`.
