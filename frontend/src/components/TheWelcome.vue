<script setup>
import { useHome } from '../composables/useHome'

const { quizes } = useHome()
</script>

<template>
  <div>
    <div v-for="quiz in quizes">
      <RouterLink :to="{ name: 'quiz', params: { id: quiz.id } }">{{
        quiz.title
      }}</RouterLink>
    </div>
  </div>
</template>
