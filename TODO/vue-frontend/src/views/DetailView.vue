<script>
import { RouterLink, RouterView } from 'vue-router'
import axios from "axios"
import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore,
        }
    },

    components: {
        RouterLink,
    },

    data() {
        return {
            todo: [],
        };
    },

    mounted() {
        this.getTodo();
    },

    methods: {
        async getTodo() {
            const config = {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('user.access')}`,
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                }
            };
            await axios.get(`/todo/detail/${this.$route.params.id}/`, config)
                .then(response => {
                    this.todo = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        logout() {
            this.userStore.removeToken()
            location.assign('/login')
        },
    },

}

</script>

<template>

    <main class="pt-8 pb-4 lg:pt-4 lg:pb-4 bg-gray-50 dark:bg-gray-900 antialiased">
        <div class="flex justify-between px-4 mx-auto max-w-screen-xl ">
            <article
                class="mx-auto w-full max-w-2xl format format-sm sm:format-base lg:format-lg format-blue dark:format-invert">
                <header class="mb-4 lg:mb-6 not-format">
                    <address class="flex items-center mb-6 not-italic">
                        <div class="inline-flex items-center mr-3 text-sm text-gray-900 dark:text-white">
                            <div class="mr-6 rounded-full">
                                <RouterLink :to="{ name: 'home' }"
                                    class="text-sm text-gray-700 bg-gray-100 rounded-full dark:bg-gray-800 dark:text-white hover:bg-gray-200 dark:hover:bg-gray-700">
                                    <span
                                        class="text-xs inline-flex bg-primary-600 rounded-full text-white px-5 py-1.5">
                                        <svg class="w-6 h-6 text-white dark:text-gray-900" aria-hidden="true"
                                            xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none"
                                            viewBox="0 0 24 24">
                                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                                stroke-width="2" d="M5 12h14M5 12l4-4m-4 4 4 4" />
                                        </svg>
                                    </span>
                                </RouterLink>
                            </div>
                            <div>
                                <a href="#" rel="author" class="text-xl font-bold text-gray-900 dark:text-white">
                                    {{ todo.author ? todo.author.first_name + ' ' + todo.author.last_name : '' }}
                                </a>
                                <p class="text-base text-gray-500 dark:text-gray-400">
                                    {{ todo.author ? todo.author.username : '' }}
                                </p>
                                <p class="text-base text-gray-500 dark:text-gray-400">
                                    <time>
                                        {{ todo.author ? todo.author.email : '' }}
                                    </time>
                                </p>
                            </div>
                        </div>
                    </address>
                    <h1
                        class="mb-4 text-3xl font-extrabold leading-tight text-gray-900 lg:mb-6 lg:text-4xl dark:text-white">
                        {{ todo.name }}
                    </h1>
                </header>
                <p class="lead">
                <div v-html="todo.body"></div>
                </p>
            </article>
        </div>
    </main>

</template>