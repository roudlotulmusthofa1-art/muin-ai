<!-- Satu baris kitab. Dipakai di tab Bidang, Mu'allif, dan Kitab. -->
<script setup>
import KotakCentang from './KotakCentang.vue'

defineProps({
  kitab: { type: Object, required: true },
  namaMuallif: { type: String, default: '' },
  terpilih: { type: Boolean, default: false },
  radio: { type: Boolean, default: false }, // true = mode Studi Satu Kitab
  terkunci: { type: Boolean, default: false }, // true = hanya bisa dilihat
  menjorok: { type: Boolean, default: false }, // geser ke kanan di bawah grup
})

const emit = defineEmits(['ubah'])
</script>

<template>
  <button
    type="button"
    :role="radio ? 'radio' : 'checkbox'"
    :aria-checked="terpilih"
    :disabled="terkunci"
    class="flex w-full items-center gap-3 border-t border-garis/70 py-2.5 pr-3 text-left transition first:border-t-0 enabled:hover:bg-krem-muda disabled:cursor-default"
    :class="menjorok ? 'pl-10' : 'pl-4'"
    @click="emit('ubah')"
  >
    <KotakCentang :keadaan="terpilih ? 'penuh' : 'kosong'" :bentuk="radio ? 'bulat' : 'kotak'" />

    <div class="min-w-0 flex-1">
      <p class="truncate text-[13px] text-navy">{{ kitab.judul }}</p>
      <p class="truncate text-[11px] text-ink-soft">{{ namaMuallif }}</p>
    </div>

    <span class="shrink-0 text-[11px] text-ink-faint">{{ kitab.label }}</span>
  </button>
</template>
