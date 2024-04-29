<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { RouterLink } from 'vue-router'

export default {
    setup() {
        const userStore = useUserStore();
        return {
            userStore,
        };
    },
    data() {
        return {
            form: {
                username: '',
                password: ''
            },
            errors: [],
            msg: false,
        };
    },
    methods: {
        async submitForm() {
            this.errors = [];
            if (this.form.username === '') {
                this.errors.push('Iltimos usernameni kiriting');
            }
            if (this.form.username.length <= 3) {
                this.errors.push("Username 3 belgidan ko'proq bo'lish kerak");
            }
            if (this.form.password === '') {
                this.errors.push('Iltimos parolni kiriting');
            }
            if (this.form.password.length <= 6) {
                this.errors.push("Parol 6 belgidan ko'proq bo'lish kerak");
            }
            if (this.errors.length === 0) {
                this.msg = true;
                try {
                    const response = await axios.post('/user/login/', this.form);
                    this.userStore.setToken(response.data)
                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    
                } catch (error) {
                    this.errors.push('Username yoki parol xato.');
                }
            }
            if (this.errors.length === 0) {
                await axios
                    .get('/user/me/')
                    .then(response => {
                        this.userStore.setUserInfo(response.data['user']);

                        location.assign('/')
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        }
    },
    components: { RouterLink },

    beforeRouteEnter(to, from, next) {
        window.scrollTo(0, 0);
        next();
    }
}
</script>

<template>
    <section class="bg-gray-50 dark:bg-gray-900">
        <div class="flex flex-col items-center justify-center mt-3">
            <div
                class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1
                        class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                        Login your account
                    </h1>
                    <form v-on:submit.prevent="submitForm" class="space-y-4 md:space-y-6" action="#">
                        <div>
                            <label for="username" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                Username
                            </label>
                            <input v-model="form.username" type="text" name="username" id="username"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                placeholder="username">
                        </div>
                        <div>
                            <label for="password"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                            <input v-model="form.password" type="password" name="password" id="password"
                                placeholder="••••••••"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                        </div>
                        <button type="submit"
                            class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                            Login
                        </button>
                        <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                            Create an account.
                            <RouterLink :to="{ name: 'signup' }"
                                class="font-medium text-primary-600 hover:underline dark:text-primary-500">
                                Sign Up
                            </RouterLink>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>