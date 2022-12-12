import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
export const useSignIn = () => {
  const router = useRouter()
  const store = useAuthStore()

  const username = ref('')
  const password = ref('')

  const submitForm = async () => {
    axios.defaults.headers.common['Authorization'] = ''
    localStorage.removeItem('access_token')
    const formData = {
      username: username.value,
      password: password.value,
    }
    try {
      const response = await axios.post('/api/v1/auth/jwt/create/', formData)
      console.log(response)
      const access_token = response.data.access
      const refresh_token = response.data.refresh

      store.setAccessToken(access_token)
      store.setRefreshToken(refresh_token)

      axios.defaults.headers.common['Authorization'] = `JWT ${access_token}`
      localStorage.setItem('access_token', access_token)
      localStorage.setItem('refresh_token', refresh_token)

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
