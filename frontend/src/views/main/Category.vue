<template>
  <div class="all- posts">
    <h1 class="text-5xl font-extrabold mb-2">Название категории</h1>
    <p class="text-gray-500 text-lg mb-5">
      Множество статей о том, как Данил Крисько, Олег Либих и Данил Башкайкин
      занимаются спортом!
    </p>

    <post-list :posts="this.postsByCategory"></post-list>

    <div class="space-y-2 pt-6 pb-8 md:space-y-5">
      <nav class="flex justify-between">
        <button rel="previous" class="hover:underline hover:text-blue-700">
          Предыдущая
        </button>
        <span>1 of 2</span>
        <button rel="next" class="hover:underline hover:text-blue-700">
          Следующая
        </button>
      </nav>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import PostList from "@/components/PostList.vue";
import { POSTS_BY_CATEGORY } from "@/queries";

export default {
  components: { PostList },
  name: "CategoryView",

  data() {
    return {
      postsByCategory: null,
    };
  },

  async created() {
    const posts = await this.$apollo.query({
      query: POSTS_BY_CATEGORY,
      variables: {
        category: this.$route.params.category,
      },
    });
    this.postsByCategory = posts.data.postsByCategory;
  },
};
</script>
