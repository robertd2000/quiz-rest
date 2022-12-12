import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import App from './App.vue'
import router from './router'

import './assets/main.css'

const app = createApp(App)

axios.defaults.baseURL = 'http://127.0.0.1:8000'

app.use(createPinia())
app.use(router, axios)

app.mount('#app')
