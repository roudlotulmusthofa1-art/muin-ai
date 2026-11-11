<script setup>
import logo from '../assets/logo.svg'

defineProps({
  tagline: {
    type: String,
    default: 'Riset berbasis sumber, dengan ibarah dan sitasi yang dapat diperiksa.',
  },
})
</script>

<template>
  <section class="flex flex-col items-center text-center">
    <div class="relative w-52 h-40 flex items-center justify-center">
      <!-- Orbit dekoratif -->
      <svg class="absolute inset-0 w-full h-full text-navy/15" viewBox="0 0 208 160" fill="none">
        <ellipse cx="104" cy="70" rx="98" ry="52" stroke="currentColor" stroke-width="1" transform="rotate(-18 104 70)" />
        <ellipse cx="104" cy="70" rx="98" ry="52" stroke="currentColor" stroke-width="1" transform="rotate(20 104 70)" />
        <circle cx="152" cy="10" r="3" fill="#1f6b4a" />
        <circle cx="183" cy="60" r="2.5" fill="#1f6b4a" />
      </svg>
      <img :src="logo" alt="Muin AI" class="relative w-36 h-auto" />
    </div>

    <p class="mt-10 max-w-lg font-serif text-xl md:text-2xl leading-relaxed text-ink-soft">
      {{ tagline }}
    </p>
  </section>
</template>
