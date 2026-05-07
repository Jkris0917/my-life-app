import api from './api'

export const login = async (username: string, password: string) => {
    // hint: POST to '/token/' with username and password
    // hint: store the access token in localStorage with key 'token'
    // hint: return the response data
    const response = await api.post('/token/', { username, password })
    const { access } = response.data
    localStorage.setItem('token', access)
    return response.data
}

export const logout = () => {
    // hint: remove the token from localStorage
    localStorage.removeItem('token')
}

export const isAuthenticated = () => {
    // hint: check if token exists in localStorage
    // hint: return true or false
    return !!localStorage.getItem('token')
}