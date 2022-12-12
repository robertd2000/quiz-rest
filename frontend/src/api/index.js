import axios from 'axios'

export class Api {
  static async getQuizes() {
    const response = await axios.get('/api/v1/')
    return await response.data
  }

  static async getQuiz(id) {
    const response = await axios.get(`/api/v1/${id}/`)
    return await response.data
  }

  static async postResults(id, results) {
    const response = await axios.post(`/api/v1/${id}/results/`, results)
    return await response.data
  }
}
