<template>
  <div class="flex flex-col min-h-screen">
    <header class="w-full bg-gray-900 text-white py-6">
      <div class="max-w-7xl mx-auto flex items-center justify-between px-4 sm:px-6 xl:px-8">
        <div class="flex items-center space-x-4">
          <div class="text-3xl font-extrabold tracking-tight">
            <router-link to="/" v-if="mySite">{{ mySite.name }}</router-link>
          </div>
          <nav class="hidden sm:flex space-x-4">
            <router-link to="/" class="text-lg font-medium hover:text-blue-400">Главная</router-link>
            <router-link to="/categories" class="text-lg font-medium hover:text-blue-400">Категории</router-link>
            <router-link to="/tags" class="text-lg font-medium hover:text-blue-400">Теги</router-link>
            <router-link v-if="user.isAuthenticated" to="/profile" class="text-lg font-medium hover:text-blue-400">Профиль</router-link>
          </nav>
        </div>
        <div class="hidden sm:flex items-center space-x-4">
          <router-link v-if="!user.isAuthenticated" to="/signin" class="text-lg font-medium hover:text-blue-400">Авторизация</router-link>
          <button v-if="user.isAuthenticated" @click="userSignOut" class="text-lg font-medium hover:text-blue-400">Выйти</button>
        </div>
        <div class="sm:hidden">
          <button @click="menuOpen = !menuOpen" class="text-white focus:outline-none">
            <i v-if="menuOpen" class="fa-solid fa-xmark"></i>
            <i v-else class="fa-solid fa-bars"></i>
          </button>
          <div v-if="menuOpen" class="absolute top-16 right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5">
            <router-link to="/" class="block px-4 py-2 text-lg text-gray-700 hover:bg-gray-100">Главная</router-link>
            <router-link to="/categories" class="block px-4 py-2 text-lg text-gray-700 hover:bg-gray-100">Категории</router-link>
            <router-link to="/tags" class="block px-4 py-2 text-lg text-gray-700 hover:bg-gray-100">Теги</router-link>
            <router-link v-if="user.isAuthenticated" to="/profile" class="block px-4 py-2 text-lg text-gray-700 hover:bg-gray-100">Профиль</router-link>
            <router-link v-if="!user.isAuthenticated" to="/signin" class="block px-4 py-2 text-lg text-gray-700 hover:bg-gray-100">Авторизация</router-link>
            <button v-if="user.isAuthenticated" @click="userSignOut" class="block w-full text-left px-4 py-2 text-lg text-gray-700 hover:bg-gray-100">Выйти</button>
          </div>
        </div>
      </div>
    </header>

    <main class="flex-grow container mx-auto max-w-7xl px-4 sm:px-6 xl:px-8">
      <router-view />
    </main>

    <footer class="w-full bg-gray-900 text-white py-6">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 xl:px-8 text-center text-sm space-x-2">
        <a class="hover:underline">DOD</a>
        <span>•</span>
        <span>© 2024</span>
        <span>•</span>
        <a href="/" class="hover:underline">Влоги о спорте</a>
      </div>
    </footer>
  </div>
</template>

<script>
import { SITE_INFO } from "@/queries";
import { useUserStore } from "@/stores/user";

export default {
  setup() {
    const userStore = useUserStore();
    return { userStore };
  },

  data() {
    return {
      menuOpen: false,
      mySite: null,
      user: {
        isAuthenticated: false,
        token: this.userStore.getToken || "",
        info: this.userStore.getUser || {},
      },
      dataLoaded: false,
    };
  },

  async created() {
    const siteInfo = await this.$apollo.query({
      query: SITE_INFO,
    });
    this.mySite = siteInfo.data.site;

    if (this.user.token) {
      this.user.isAuthenticated = true;
    }
  },

  methods: {
    userSignOut() {
      this.userStore.removeToken();
      this.userStore.removeUser();
      this.user.isAuthenticated = false;
    },
  },
};
</script>
