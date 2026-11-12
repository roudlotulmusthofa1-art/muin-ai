import { ref } from 'vue'

// Fitur salin ke clipboard yang bisa dipakai di mana saja.
// Setelah tombol diklik, hasil berisi { kunci, berhasil } selama 1,5 detik,
// jadi tombol yang diklik bisa menampilkan "Tersalin ✓" atau "Gagal menyalin".
export function useSalin() {
  const hasil = ref({ kunci: '', berhasil: false })
  let timer = null

  async function salin(teks, kunci = 'default') {
    try {
      await navigator.clipboard.writeText(teks)
      hasil.value = { kunci, berhasil: true }
    } catch {
      // Bisa gagal kalau browser tidak mengizinkan akses clipboard
      hasil.value = { kunci, berhasil: false }
    }
    clearTimeout(timer)
    timer = setTimeout(() => (hasil.value = { kunci: '', berhasil: false }), 1500)
  }

  // Teks tombol: normal / "Tersalin ✓" / "Gagal menyalin"
  function labelTombol(kunci, teksNormal) {
    if (hasil.value.kunci !== kunci) return teksNormal
    return hasil.value.berhasil ? 'Tersalin ✓' : 'Gagal menyalin'
  }

  return { salin, labelTombol }
}
