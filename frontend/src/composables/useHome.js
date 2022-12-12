import { onMounted, ref } from 'vue'
import { Api } from '../api'

export const useHome = () => {
  const quizes = ref(null)

  onMounted(async () => {
    const result = await Api.getQuizes()
    quizes.value = result
  })

  return {
    quizes,
  }
}
