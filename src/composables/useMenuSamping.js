import { ref } from 'vue'

// =====================================================================
// State menu samping (sidebar).
// Ditaruh DI LUAR fungsi supaya semua komponen memakai state yang SAMA:
// tombol ☰ di halaman mana pun membuka/menutup, MenuSamping.vue menampilkannya.
//
// Karena state ini tidak ikut di-reset saat pindah halaman, menu yang
// sudah dibuka tetap terbuka walaupun pindah halaman (seperti di Claude).
// Ganti false → true kalau mau menu langsung terbuka saat aplikasi dibuka.
// =====================================================================
const menuTerbuka = ref(false)

export function useMenuSamping() {
  function bukaMenu() {
    menuTerbuka.value = true
  }

  function tutupMenu() {
    menuTerbuka.value = false
  }

  // Buka kalau sedang tertutup, tutup kalau sedang terbuka
  function gantiMenu() {
    menuTerbuka.value = !menuTerbuka.value
  }

  return { menuTerbuka, bukaMenu, tutupMenu, gantiMenu }
}
