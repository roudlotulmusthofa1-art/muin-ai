import { createRouter, createWebHistory } from 'vue-router'
import { useSesiChat } from '../composables/useSesiChat'

// =====================================================================
// ROUTER = "peta alamat" aplikasi.
// Setiap alamat (path) di browser dipasangkan dengan satu halaman.
//
//   localhost:5173/          → HalamanBeranda
//   localhost:5173/chat      → HalamanChat
//   localhost:5173/riwayat   → HalamanRiwayat
//   localhost:5173/ekspor    → HalamanEkspor
//   localhost:5173/akun      → HalamanAkun
//   ...
//
// "component: () => import(...)" artinya halaman baru DIMUAT saat dibuka
// (lazy loading), jadi aplikasi terbuka lebih cepat di awal.
// =====================================================================

const routes = [
  {
    path: '/',
    name: 'beranda',
    component: () => import('../halaman/HalamanBeranda.vue'),
  },
  {
    path: '/chat',
    name: 'chat',
    component: () => import('../halaman/HalamanChat.vue'),
    // "Penjaga pintu": dijalankan SEBELUM halaman chat dibuka.
    // Kalau belum ada pertanyaan (misal halaman di-refresh), kembalikan ke beranda.
    beforeEnter: () => {
      const { pertanyaanAktif } = useSesiChat()
      if (!pertanyaanAktif.value) return { name: 'beranda' }
    },
  },

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
  // Alamat yang tidak dikenal (misal /asal-ketik) → kembali ke beranda
  { path: '/:pathMatch(.*)*', redirect: { name: 'beranda' } },
]

const router = createRouter({
  // createWebHistory = alamat biasa tanpa tanda "#" (localhost:5173/chat)
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
