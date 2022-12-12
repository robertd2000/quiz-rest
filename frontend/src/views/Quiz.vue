<script setup>
import { useRoute, useRouter } from 'vue-router'
import Answers from '../components/Answers.vue'
import Modal from '../components/Modal.vue'

import { useQuiz } from '../composables/useQuiz'

const route = useRoute()

const { loading, currentQuestion, next, score, isEnd, setAnswer } = useQuiz(
  route.params.id
)

const toNext = () => {
  if (!isEnd.value) {
    next()
  }
}
</script>

<template>
  <div class="quiz">
    <div class="card" style="width: 100%" v-if="!loading">
      <h5 class="card-header">{{ currentQuestion?.title }}</h5>
      <div class="card-body">
        <Answers
          :answers="currentQuestion?.answer_set"
          @setAnswer="setAnswer"
        />
        <button class="btn btn-success" v-if="!isEnd" @click="toNext">
          Ответить
        </button>
      </div>
    </div>

    <Modal :score="score" :isEnd="isEnd" />
  </div>
</template>

<style>
.quiz {
  max-width: 1000px;
  margin: 30px auto;
}
.card {
  width: 800px !important;
}

@media (max-width: 1050px) {
  .card {
    width: 500px !important;
  }
}
</style>
