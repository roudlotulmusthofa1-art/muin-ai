<!--
  Halaman chat. File ini hanya MENYUSUN komponen-komponen kecil:

  ┌ BannerPrototipe ─────────────────────────────────────────────┐
  │ SidebarChat │ KepalaChat                                      │
  │             ├───────────────────────────────┬─────────────────┤
  │             │ BilahKonteks                  │ PanelBukti      │
  │             │ KartuPertanyaan               │ (kalau chip     │
  │             │ Status... / HasilJawaban      │  sitasi diklik) │
  │             │ KolomChat                     │                 │
  └─────────────┴───────────────────────────────┴─────────────────┘
-->
<script setup>
import { useSesiChat } from '../composables/useSesiChat'
import KepalaChat from '../components/chat/KepalaChat.vue'
import BilahKonteks from '../components/chat/BilahKonteks.vue'
import KartuPertanyaan from '../components/chat/KartuPertanyaan.vue'
import StatusBerjalan from '../components/chat/StatusBerjalan.vue'
import HasilJawaban from '../components/chat/HasilJawaban.vue'
import StatusBelumCukup from '../components/chat/StatusBelumCukup.vue'
import StatusGangguan from '../components/chat/StatusGangguan.vue'
import StatusDibatalkan from '../components/chat/StatusDibatalkan.vue'
import KolomChat from '../components/chat/KolomChat.vue'
import PanelBukti from '../components/chat/PanelBukti.vue'
import PilihSkenarioDemo from '../components/chat/PilihSkenarioDemo.vue'

const { status, sitasiAktif } = useSesiChat()
</script>

<template>
  <!-- h-screen + min-h-0: supaya hanya bagian tengah yang bisa di-scroll -->
  <div class="flex h-full flex-col bg-[#F7F2E8]">


    <div class="flex min-h-0 flex-1">
      

      <div class="flex min-w-0 flex-1 flex-col">
        <KepalaChat />

        <div class="flex min-h-0 flex-1">
          <!-- KOLOM TENGAH (bisa di-scroll) -->
          <main class="min-w-0 flex-1 overflow-y-auto px-4 sm:px-8">
            <div class="mx-auto max-w-[810px] pt-7">
              <div class="space-y-5">
                <BilahKonteks />
                <KartuPertanyaan />

                <!-- Hanya SATU yang tampil, tergantung status riset -->
                <StatusBerjalan v-if="status === 'berjalan'" />
                <HasilJawaban v-else-if="status === 'selesai'" />
                <StatusBelumCukup v-else-if="status === 'belum-cukup'" />
                <StatusGangguan v-else-if="status === 'gangguan'" />
                <StatusDibatalkan v-else-if="status === 'dibatalkan'" />
              </div>

              <KolomChat />
            </div>
          </main>

          <!-- PANEL KANAN -->
          <PanelBukti v-if="sitasiAktif" />
        </div>
      </div>
    </div>

    <PilihSkenarioDemo />

    <span
      class="pointer-events-none fixed right-3 bottom-3 rounded-full border border-black/10 bg-white/70 px-3 py-1 text-[10px] font-semibold tracking-wider text-ink-faint uppercase"
    >
      Prototipe UI v0.3 · Data Sintetis
    </span>
  </div>
</template>
