<script setup>
import { defineProps } from 'vue'

const props = defineProps(['score', 'isEnd'])
</script>

<template>
  <div v-show="isEnd" class="modal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Результат</h5>
        </div>
        <div class="modal-body">
          <p>
            Правильных ответов {{ score?.right_answers }} из
            {{ score?.total_answers }}
          </p>
          <p>
            Неправильных ответов {{ score?.wrong_answers }} из
            {{ score?.total_answers }}
          </p>
          <p>Процент правильных ответов: {{ score?.percent_right }}</p>
          <p>Процент неправильных ответов: {{ score?.percent_wrong }}</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-success">
            <RouterLink :to="{ name: 'home' }">Домой</RouterLink>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal {
  display: block;
}

a {
  color: white;
}
</style>
