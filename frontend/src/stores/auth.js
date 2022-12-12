import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('counter', () => {
  const access_token = ref('')
  const refresh_token = ref('')
  const user = ref('')

  const initialize = () => {
    if (localStorage.getItem('access_token')) {
      access_token.value = localStorage.getItem('access_token')
      refresh_token.value = localStorage.getItem('refresh_token')
    } else {
      access_token.value = ''
      refresh_token.value = ''
    }
  }

  const setAccessToken = (token) => {
    access_token.value = token
  }

  const setRefreshToken = (token) => {
    refresh_token.value = token
  }

  const setUser = async () => {
    try {
      const response = await axios.get('/api/v1/auth/users/me')
      user.value = response.data.username
    } catch (error) {
      console.log('auth user', error)
    }
  }

  return {
    access_token,
    refresh_token,
    user,
    initialize,
    setAccessToken,
    setRefreshToken,
    setUser,
  }
})
