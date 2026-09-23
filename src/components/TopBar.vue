<script setup>

const emit = defineEmits([
  'toggle-menu',
  'open-history',
  'change-language',
  'open-profile',
  'toggle-research-menu'
])

defineProps({
  historyLabel: {
    type: String,
    default: 'Riwayat 3 Hari'
  },

  language: {
    type: String,
    default: 'ID'
  }
})

</script>

<template>

  <header
    class="flex items-center justify-between px-6 md:px-16 py-6"
  >

    <!-- HAMBURGER -->
    <button
      type="button"
      class="p-1 rounded-md text-ink hover:bg-black/5 hover:text-[#1e5e38] transition"
      aria-label="Buka menu"
      @click="emit('toggle-research-menu')"
    >

      <svg
        width="22"
        height="22"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="1.8"
        stroke-linecap="round"
      >
        <path d="M4 7h16M4 12h16M4 17h16" />
      </svg>

    </button>


    <!-- NAVIGASI -->
    <nav
      class="flex items-center gap-8 text-sm font-semibold text-ink"
    >

      <!-- RIWAYAT -->
      <button
        type="button"
        class="hover:text-[#1e5e38] transition"
        @click="emit('open-history')"
      >
        {{ historyLabel }}
      </button>


      <!-- BAHASA -->
      <button
        type="button"
        class="flex items-center gap-2 hover:text-[#1e5e38] transition"
        @click="emit('change-language')"
      >

        <svg
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="1.6"
        >
          <circle
            cx="12"
            cy="12"
            r="9"
          />

          <path
            d="M3 12h18M12 3c2.8 3 2.8 15 0 18M12 3c-2.8-3-2.8-15 0-18"
          />
        </svg>

        <span>
          {{ language }}
        </span>

      </button>


      <!-- PROFILE -->
      <button
        type="button"
        class="hover:text-[#1e5e38] transition"
        aria-label="Profil"
        @click="emit('open-profile')"
      >

        <svg
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="1.6"
          stroke-linecap="round"
        >
          <circle
            cx="12"
            cy="8"
            r="4"
          />

          <path
            d="M4 21c0-4 3.6-6.5 8-6.5s8 2.5 8 6.5"
          />
        </svg>

      </button>

    </nav>

  </header>

</template>