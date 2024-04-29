import { defineStore } from "pinia"
import axios from "axios"


export const useUserStore = defineStore({
    id: 'user',

    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            username: null,
            email: null,
            access: null,
            refresh: null
        }
    }),

    actions: {
        initStore() {
            if (localStorage.getItem('user.access')) {
                console.log('User has access')

                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.email = localStorage.getItem('user.email')
                this.user.username = localStorage.getItem('user.username')

                this.refreshToken()
            }
        },

        setToken(data) {
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)
        },

        setUserInfo(user) {
            this.user.id = user.id
            this.user.email = user.email
            this.user.username = user.username

            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.username', this.user.username)
        },

        removeToken() {
            this.user.access = null
            this.user.refresh = null
            this.user.id = null
            this.user.email = null
            this.user.username = null

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.username', '')
        },

        refreshToken() { 
            axios.post('/user/refresh/', {
                refresh: this.user.refresh
            })

                .then((response) => {
                    this.user.access = response.data.access

                    localStorage.setItem('user.access', response.data.access)

                    axios.defaults.headers.common["Authorization"] = "Bearer" + response.data.access
                })
                .catch((error) => {
                    this.removeToken()
                })
        },
    }
})