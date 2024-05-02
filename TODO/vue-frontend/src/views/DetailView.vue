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
            form: {
                body: '',
            }
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
                    this.form.body = this.todo.body
                })
                .catch(error => {
                    console.log(error)
                })
        },
        logout() {
            this.userStore.removeToken()
            location.assign('/login')
        },
        async updateTodo() {
            const config = {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('user.access')}`,
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                }
            };

            const updateData = {
                name: this.todo.name,
                body: this.form.body
            };

            try {
                const response = await axios.put(`/todo/detail/${this.$route.params.id}/`, updateData, config);
                this.todo = response.data;
                this.$router.push('/');
            } catch (error) {
                if (error.response && error.response.status === 400) {
                    const validationErrors = error.response.data;
                    console.error('Validation Errors:', validationErrors);
                } else {
                    console.error('Server Error:', error.response.status, error.response.data);
                }
            }

        },
        submit() {
            this.updateTodo();
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
                                <a @click="submit"
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
                                </a>
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
                </header>
                <p class="lead">
                <div class="sm:col-span-2">
                    <label for="description" class="block mb-2 text-sm font-medium text-gray-900">
                        <h1
                            class="mb-4 text-3xl font-extrabold leading-tight text-gray-900 lg:mb-6 lg:text-4xl dark:text-white">
                            {{ todo.name }}
                        </h1>
                    </label>
                    <textarea id="description" rows="8"
                        class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-50"
                        v-model="form.body"></textarea>
                </div>
                </p>
            </article>
        </div>
    </main>

</template>