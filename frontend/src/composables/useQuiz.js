import { onMounted, ref } from 'vue'
import { Api } from '../api'

export const useQuiz = (id) => {
  const quiz = ref(null)
  const loading = ref(false)
  const questions = ref([])
  const currentQuestion = ref(null)
  const currentQuestionId = ref(0)
  const results = ref([])
  const score = ref(null)
  const isEnd = ref(false)
  const answer = ref('')

  onMounted(async () => {
    loading.value = true
    const result = await Api.getQuiz(id)
    quiz.value = result
    questions.value = result?.question_set
    currentQuestion.value = questions.value[currentQuestionId.value]
    loading.value = false
  })

  const setAnswer = (text) => {
    answer.value = text
  }

  const next = () => {
    results.value.push(answer.value)
    if (
      questions.value &&
      questions.value.length - 1 > currentQuestionId.value &&
      answer.value
    ) {
      currentQuestionId.value++
      currentQuestion.value = questions.value[currentQuestionId.value]
      answer.value = ''
    } else if (questions.value.length - 1 <= currentQuestionId.value) {
      isEnd.value = true
      endGame()
    }
  }

  const endGame = async () => {
    const result = await Api.postResults(id, results.value)
    score.value = result
  }

  return {
    questions,
    currentQuestion,
    next,
    isEnd,
    setAnswer,
    score,
    loading,
  }
}
