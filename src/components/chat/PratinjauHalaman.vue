<!-- Tab halaman (Sebelumnya · Aktif · Berikutnya) + tampilan halaman kitab dengan teks Arab -->
<script setup>
import { ref, computed } from 'vue'
import { teksHalaman } from '../../data/dataSitasi'

const props = defineProps({
  sitasi: { type: Object, required: true },
})

// Halaman yang sedang dilihat. Awalnya = halaman yang dikutip.
const halamanDilihat = ref(props.sitasi.halaman)

const daftarTab = computed(() => [
  { label: 'Sebelumnya', halaman: props.sitasi.halaman - 1 },
  { label: 'Aktif', halaman: props.sitasi.halaman },
  { label: 'Berikutnya', halaman: props.sitasi.halaman + 1 },
])

const teks = computed(() => teksHalaman(props.sitasi, halamanDilihat.value))
</script>

<template>
  <div>
    <div class="grid grid-cols-3 gap-2" role="tablist" aria-label="Pilih halaman">
      <button
        v-for="tab in daftarTab"
        :key="tab.halaman"
        type="button"
        role="tab"
        :aria-selected="halamanDilihat === tab.halaman"
        class="rounded-md border px-2 py-2.5 text-xs transition"
        :class="
          halamanDilihat === tab.halaman
            ? 'border-hijau bg-white font-semibold text-navy shadow-[inset_0_-3px_0_var(--color-hijau)]'
            : 'border-garis bg-kertas text-ink-soft hover:bg-white'
        "
        @click="halamanDilihat = tab.halaman"
      >
        {{ tab.label }} · {{ tab.halaman }}
      </button>
    </div>

    <!-- "Kertas" halaman kitab -->
    <div class="mt-4 min-h-80 rounded-sm border border-garis bg-kertas px-6 py-5 shadow-sm">
      <p class="text-right text-xs text-ink-soft">{{ halamanDilihat }}</p>
      <p class="mt-2 border-b border-garis pb-2 text-right text-xs font-semibold text-hijau">{{ sitasi.bab }}</p>

      <!-- dir="rtl" = kanan ke kiri, lang="ar" = bahasa Arab -->
      <p dir="rtl" lang="ar" class="mt-5 font-serif text-2xl leading-[2.4] text-ink">
        {{ teks.sebelum }}<mark v-if="teks.sorot" class="rounded bg-hijau-muda px-0.5 text-ink">{{ teks.sorot }}</mark>{{ teks.sesudah }}
      </p>
    </div>
  </div>
</template>
