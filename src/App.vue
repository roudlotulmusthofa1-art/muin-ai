<script setup>
import { ref } from 'vue'
import BannerPrototipe from './components/BannerPrototipe.vue'
import BilahAtas from './components/BilahAtas.vue'
import HeroMerek from './components/HeroMerek.vue'
import ChipSaran from './components/ChipSaran.vue'
import DropdownPilihan from './components/DropdownPilihan.vue'
import TombolRiset from './components/TombolRiset.vue'
import KolomTanya from './components/KolomTanya.vue'
import ModalRiset from './components/riset/ModalRiset.vue'
import { usePertanyaan, PILIHAN_CAKUPAN, SARAN } from './composables/usePertanyaan'
import { useRiset } from './composables/useRiset'

const { pertanyaan, cakupan, sedangMengirim, terakhirDikirim, bisaKirim, pakaiSaran, kirim } = usePertanyaan()
const { modalTerbuka } = useRiset()

const kolomTanya = ref(null)

function pilihSaran(teks) {
  pakaiSaran(teks)
  kolomTanya.value?.focus()
}
</script>

<template>
  <div class="flex min-h-screen flex-col bg-[#F7F2E8]">
    <BannerPrototipe />

    <BilahAtas />

    <main class="flex flex-1 flex-col items-center justify-center px-4 pb-20">
      <HeroMerek />

      <div class="mt-14 flex w-full flex-col items-center gap-3.5">
        <ChipSaran :items="SARAN" @select="pilihSaran" />

        <!-- Cakupan + tombol pembuka modal riset -->
        <div class="flex max-w-full flex-wrap justify-center gap-2.5">
          <DropdownPilihan v-model="cakupan" :options="PILIHAN_CAKUPAN" />
          <TombolRiset />
        </div>

        <div class="mt-1.5 flex w-full justify-center">
          <KolomTanya
            ref="kolomTanya"
            v-model="pertanyaan"
            :disabled="!bisaKirim"
            :loading="sedangMengirim"
            @submit="kirim"
          />
        </div>

        <p v-if="terakhirDikirim" class="mt-4 text-xs text-ink-soft">
          Pertanyaan terkirim: "{{ terakhirDikirim.pertanyaan }}"
        </p>
      </div>
    </main>

    <footer class="flex justify-end px-4 pb-4">
      <span
        class="rounded-full border border-black/10 bg-white/60 px-3 py-1 text-[10px] font-semibold tracking-wider text-ink-faint uppercase"
      >
        Prototipe UI v0.3 · Data Sintetis
      </span>
    </footer>

    <!-- MODAL ATUR RISET (muncul saat TombolRiset diklik) -->
    <Transition
      enter-active-class="transition duration-150 ease-out"
      enter-from-class="opacity-0"
      leave-active-class="transition duration-100 ease-in"
      leave-to-class="opacity-0"
    >
      <ModalRiset v-if="modalTerbuka" />
    </Transition>
  </div>
</template>
