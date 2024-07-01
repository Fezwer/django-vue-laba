<template>
  <div class="flex items-center justify-center h-screen w-full sm:w-2/3 md:w-1/3 mx-auto">
    <form action="POST" @submit.prevent="userSignIn()" class="w-full max-h-screen overflow-auto">
      <div class="bg-white rounded-xl w-full p-6">
        <div class="space-y-4">
          <div>
            <label for="username" class="block mb-1 text-gray-600 font-medium">Имя пользователя</label>
            <input
              type="text"
              id="username"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50"
              v-model="signInDetails.username"
            />
          </div>
          <div>
            <label for="password" class="block mb-1 text-gray-600 font-medium">Пароль</label>
            <input
              type="password"
              id="password"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50"
              v-model="signInDetails.password"
            />
          </div>
        </div>
        <button
          class="mt-4 w-full bg-blue-500 hover:bg-blue-700 hover:text-blue-100 focus:ring focus:ring-teal-100 text-white py-2 rounded-md text-lg tracking-wide"
        >
          Авторизоваться
        </button>
        <div v-if="errorMessage" class="mt-2 text-red-500">
          {{ errorMessage }}
        </div>
        <div class="text-right mt-2">
          <small>
            Еще нет аккаунта? Быстрее регистрируйся!
            <router-link to="/signup" class="text-blue-500 hover:underline">Зарегистрироваться</router-link>
          </small>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { useUserStore } from "@/stores/user";
import { USER_SIGNIN } from "@/mutations";
import { useRouter } from "vue-router";

export default {
  name: "SignInView",

  setup() {
    const userStore = useUserStore();
    const router = useRouter();
    return { userStore, router };
  },

  data() {
    return {
      signInDetails: {
        username: "",
        password: "",
      },
      errorMessage: null,
    };
  },

  methods: {
    async userSignIn() {
      try {
        const user = await this.$apollo.mutate({
          mutation: USER_SIGNIN,
          variables: {
            username: this.signInDetails.username,
            password: this.signInDetails.password,
          },
        });
        this.userStore.setToken(user.data.tokenAuth.token);
        this.userStore.setUser(user.data.tokenAuth.user);
        this.router.push({ name: "Profile" }).then(() => {
          window.location.reload();
        });
      } catch (error) {
        this.errorMessage = "Неверное имя пользователя или пароль. Пожалуйста, попробуйте еще раз.";
        console.error("Ошибка авторизации:", error);
      }
    },
  },
};
</script>

<style scoped>
html, body {
  height: 50%;
  margin: 0;
  overflow: hidden;
}

#app {
  height: 100%;
}

form {
  max-height: calc(100vh - 2rem);
  overflow-y: auto;
}
</style>
