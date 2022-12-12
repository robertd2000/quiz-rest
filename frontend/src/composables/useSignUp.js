import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export const useSIgnUp = () => {
  const router = useRouter()
  const username = ref('')
  const password = ref('')

  const submitForm = async () => {
    const formData = {
      email: username.value,
      username: username.value,
      password: password.value,
    }
    try {
      const response = await axios.post('/api/v1/auth/users/', formData)
      router.push('/')
    } catch (error) {
      console.log(error)
    }
  }

  return {
    username,
    password,
    submitForm,
  }
}
