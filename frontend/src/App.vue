<template>
  <div class="container mx-auto max-w-3xl px-4 sm:px-6 xl:max-w-5xl xl:px-0">
    <div class="flex flex-col justify-between h-screen">
      <header class="flex flex-row items-center justify-between py-10">
        <div class="nav-logo text-2xl font-bold">
          <router-link to="/" v-if="mySite">{{ mySite.name }}</router-link>
        </div>
        <div class="nav-links hidden sm:block">
          <router-link
            to="/"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Главная</router-link
          >
          <router-link
            to="/categories"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Категории</router-link
          >
          <router-link
            to="/tags"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Теги</router-link
          >
          <router-link
            v-if="!user.isAuthenticated"
            to="/signin"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Авторизация</router-link
          >
          <router-link
            v-if="user.isAuthenticated"
            to="/profile"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Профиль</router-link
          >
          <a
            v-if="user.isAuthenticated"
            @click="userSignOut"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Выйти</a
          >
        </div>
        <div class="sm:hidden">
          <button
            type="button"
            class="ml-1 mr-1 h-8 w-8 rounded py-1"
            aria-label="Toggle Menu"
            @click="menuOpen = !menuOpen"
          >
            <i v-if="menuOpen" class="fa-solid fa-xmark"></i>
            <i v-else class="fa-solid fa-bars"></i>
          </button>
          <div
            :class="{ 'translate-x-full': !menuOpen }"
            class="fixed top-24 right-0 z-10 h-full w-full transform bg-gray-200 opacity-95 duration-300 ease-in-out dark:bg-gray-800"
          >
            <nav
              class="fixed mt-8 w-full h-full flex flex-col space-y-2"
              @click="menuOpen = !menuOpen"
            >
              <router-link
                to="/"
                class="pl-4 text-xl font-sans font-medium hover:underline hover:text-teal-700"
                >Главная</router-link
              >
              <router-link
                to="/categories"
                class="pl-4 text-xl font-sans font-medium hover:underline hover:text-teal-700"
                >Категории</router-link
              >
              <router-link
                to="/tags"
                class="pl-4 text-xl font-sans font-medium hover:underline hover:text-teal-700"
                >Теги</router-link
              >
              <router-link
                v-if="!user.isAuthenticated"
                to="/signin"
                class="pl-4 text-xl font-sans font-medium hover:underline hover:text-teal-700"
                >Авторизоваться</router-link
              >
              <router-link
                v-if="user.isAuthenticated"
                to="/profile"
                class="pl-4 text-xl font-sans font-medium hover:underline hover:text-teal-700"
                >Профиль</router-link
              >
              <a
                v-if="user.isAuthenticated"
                @click="userSignOut"
                class="pl-4 text-xl font-sans font-medium hover:underline hover:text-teal-700"
                >Выйти</a
              >
            </nav>
          </div>
        </div>
      </header>

      <router-view />

      <footer class="flex flex-col place-items-center mt-5 py-5 border-t-2">
        <div class="mb-3 flex space-x-1 text-sm text-gray-700">
          <div>
            <a
              href="https://www.ericsdevblog.com"
              class="hover:underline hover:text-teal-700"
              >DOD</a
            >
          </div>
          <div>•</div>
          <div>© 2024</div>
          <div>•</div>
          <a href="/" class="hover:underline hover:text-teal-700"
            >Влоги о спорте</a
          >
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import { SITE_INFO } from "@/queries";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

export default {
  setup() {
    const userStore = useUserStore();
    const router = useRouter();
    return { userStore, router };
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
      this.router.push({ name: "SignIn" }).then(() => {
        window.location.reload();
      });
    },
  },
};
</script>
