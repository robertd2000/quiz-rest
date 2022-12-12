<script setup>
import { defineProps, defineEmits } from 'vue'

const props = defineProps(['answers'])
const emit = defineEmits(['setAnswer'])

const setAnswer = (value) => {
  emit('setAnswer', value)
}
</script>

<template>
  <div
    class="input-group-text mb-3"
    v-for="answer in answers"
    :key="answer.text"
  >
    <input
      type="checkbox"
      class="form-check-input"
      @change="setAnswer(answer.text)"
    />
    <span class="card-text m-3">{{ answer.text }}</span>
  </div>
</template>
