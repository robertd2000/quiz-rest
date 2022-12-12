import axios from 'axios'
import { storeToRefs } from 'pinia'
import { onMounted } from 'vue'

import { useAuthStore } from '../stores/auth'
export const useAuth = () => {
  const store = useAuthStore()
  const { access_token, refresh_token } = storeToRefs(store)

  const getAccess = async () => {
    const accessData = {
      refresh: refresh_token.value,
    }

    try {
      const response = await axios.post('/api/v1/auth/jwt/refresh/', accessData)
      const access = await response.data.access
      localStorage.setItem('access_token', access)
      store.setAccessToken(access)
    } catch (error) {
      console.log(error)
    }
  }

  onMounted(() => {
    store.initialize()

    if (access_token.value) {
      axios.defaults.headers.common[
        'Authorization'
      ] = `JWT ${access_token.value}`
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }

    setInterval(async () => {
      getAccess()
    }, 59000)
  })
}
