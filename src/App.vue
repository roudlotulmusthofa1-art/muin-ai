<script setup>
import { RouterView } from 'vue-router'
import ModalRiset from './components/riset/ModalRiset.vue'
import BannerPrototipe from './components/BannerPrototipe.vue'
import MenuSamping from './components/MenuSamping.vue'
import { useRiset } from './composables/useRiset'

const { modalTerbuka } = useRiset()


</script>

<template>
<!-- h-screen: aplikasi setinggi layar. Banner di atas, di bawahnya: menu + halaman -->
  <div class="flex h-screen flex-col bg-[#F7F2E8]">
    <BannerPrototipe />

    <div class="flex min-h-0 flex-1">
      <!-- Menu samping (lebarnya berubah saat ☰ ditekan) -->
      <MenuSamping />

      <!-- Halaman. flex-1 = mengisi sisa lebar, jadi ikut bergeser saat menu melebar -->
      <div class="min-w-0 flex-1 overflow-y-auto">
        <RouterView />
      </div>
    </div>
  </div>

  <!-- MODAL ATUR RISET (muncul saat TombolRiset diklik) -->
    <Transition
      enter-active-class="transition duration-150 ease-out"
      enter-from-class="opacity-0"
      leave-active-class="transition duration-100 ease-in"
      leave-to-class="opacity-0"
    >
      <ModalRiset v-if="modalTerbuka" />
    </Transition>
</template>
