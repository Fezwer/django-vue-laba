<template>
  <div class="all-tags">
    <h1 class="text-5xl font-extrabold mb-2">Название тега</h1>
    <p class="text-gray-500 text-lg mb-5">
      Множество статей о том, как Данил Крисько, Олег Либих и Данил Башкайкин
      занимаются спортом!
    </p>

    <post-list :posts="postsByTag"></post-list>

  </div>
</template>

<script>
// @ is an alias to /src
import PostList from "@/components/PostList.vue";
import { POSTS_BY_TAG } from "@/queries";

export default {
  components: { PostList },
  name: "TagView",

  data() {
    return {
      postsByTag: null,
    };
  },

  async created() {
    const posts = await this.$apollo.query({
      query: POSTS_BY_TAG,
      variables: {
        tag: this.$route.params.tag,
      },
    });
    this.postsByTag = posts.data.postsByTag;
  },
};
</script>
