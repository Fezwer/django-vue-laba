<template>
  <div class="home">
    <h1 class="text-5xl font-extrabold mb-2">Последние публикации</h1>
    <p class="text-gray-500 text-lg mb-5">
      Множество статей о том, как Данил Крисько, Олег Либих и Данил Башкайкин
      занимаются спортом!
    </p>

    <post-list :posts="allPosts"></post-list>
  </div>
</template>

<script>
import PostList from "@/components/PostList.vue";
import { ALL_POSTS } from "@/queries";

export default {
  components: { PostList },
  name: "HomeView",

  data() {
    return {
      allPosts: null,
    };
  },

  async created() {
    const posts = await this.$apollo.query({
      query: ALL_POSTS,
    });
    this.allPosts = posts.data.allPosts;
  },
};
</script>
