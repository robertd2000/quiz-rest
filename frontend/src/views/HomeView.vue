<script setup>
import { onMounted } from 'vue'
import TheWelcome from '../components/TheWelcome.vue'
import { useAuthStore } from '../stores/auth'
const store = useAuthStore()

onMounted(async () => {
  store.setUser()
})
</script>

<template>
  <h1>Домашняя</h1>
  <TheWelcome />
</template>
