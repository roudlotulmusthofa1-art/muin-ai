<!--
  MENU SAMPING untuk seluruh aplikasi. Ada dua cara tampil:

  1. LAYAR BESAR (lg ke atas) → mode "DORONG", seperti Claude:
     menu adalah sebuah kolom yang lebarnya berubah 0 ↔ 240px.
     Karena isi halaman ada di sebelahnya (flex-1), saat kolom ini melebar
     isi halaman ikut TERGESER ke kanan.

  2. LAYAR KECIL (HP) → mode "LACI":
     layar terlalu sempit untuk digeser, jadi menu muncul DI ATAS isi halaman
     dengan latar gelap di belakangnya.

  Isi menunya memakai ulang SidebarChat, jadi selalu sama di kedua mode.
-->
<script setup>
import { onMounted, onUnmounted } from 'vue'
import { useMenuSamping } from '../composables/useMenuSamping'
import SidebarChat from './chat/SidebarChat.vue'

const { menuTerbuka, tutupMenu } = useMenuSamping()

// Apakah layar sedang kecil (di bawah lg = 64rem = 1024px)?
const layarKecil = () => window.matchMedia('(max-width: 63.99rem)').matches

// Mode laci (HP): klik menu / "Chat baru" → laci otomatis tertutup
function tanganiKlikLaci(event) {
  if (event.target.closest('a, button')) tutupMenu()
}

// Mode laci (HP): tombol Esc menutup laci.
// Di layar besar Esc dibiarkan, supaya tidak ikut menutup menu saat menutup modal riset.
function tanganiTombol(event) {
  if (event.key === 'Escape' && menuTerbuka.value && layarKecil()) tutupMenu()
}

onMounted(() => window.addEventListener('keydown', tanganiTombol))
onUnmounted(() => window.removeEventListener('keydown', tanganiTombol))
</script>

<template>
  <!-- ========== 1. MODE DORONG (layar besar) ========== -->
  <!--
    hidden lg:block      → hanya tampil di layar besar
    w-60 / w-0           → lebar terbuka / tertutup
    transition-[width]   → perubahan lebar dianimasikan (ini yang membuat isi halaman "bergeser" halus)
    overflow-hidden      → isi menu tidak keluar saat kolomnya mengecil
    inert                → saat tertutup, isi menu tidak bisa diklik / di-Tab
  -->
  <div
    class="hidden shrink-0 overflow-hidden transition-[width] duration-300 ease-in-out lg:block"
    :class="menuTerbuka ? 'w-60' : 'w-0'"
    :inert="!menuTerbuka"
  >
    <SidebarChat />
  </div>

  <!-- ========== 2. MODE LACI (HP) ========== -->
  <Transition
    enter-active-class="transition duration-200 ease-out"
    enter-from-class="opacity-0"
    leave-active-class="transition duration-150 ease-in"
    leave-to-class="opacity-0"
  >
    <div
      v-if="menuTerbuka"
      class="fixed inset-0 z-40 bg-black/30 lg:hidden"
      aria-hidden="true"
      @click="tutupMenu"
    />
  </Transition>

  <Transition
    enter-active-class="transition duration-200 ease-out"
    enter-from-class="-translate-x-full"
    leave-active-class="transition duration-150 ease-in"
    leave-to-class="-translate-x-full"
  >
    <div
      v-if="menuTerbuka"
      class="fixed inset-y-0 left-0 z-50 shadow-xl lg:hidden"
      role="dialog"
      aria-modal="true"
      aria-label="Menu"
      @click="tanganiKlikLaci"
    >
      <SidebarChat />
    </div>
  </Transition>
</template>
