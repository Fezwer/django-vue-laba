<template>
  <div class="post-list">
    <ul v-if="publishedPosts" class="divide-y divide-gray-200">
      <li
        class="py-12 post-item"
        v-for="post in publishedPosts"
        :key="post.title"
      >
        <article>
          <div
            class="space-y-2 xl:grid xl:grid-cols-4 xl:items-baseline xl:space-y-0"
          >
            <dl>
              <dt class="sr-only">Опубликовано</dt>
              <dd
                class="text-base font-medium leading-6 text-gray-500 dark:text-gray-400"
              >
                <time>{{ formatDate(post.createdAt) }}</time>
              </dd>
            </dl>
            <div class="space-y-5 xl:col-span-3">
              <div class="space-y-6">
                <div>
                  <h2 class="text-2xl font-bold leading-8 tracking-tight">
                    <router-link
                      class="text-gray-900"
                      :to="`/post/${post.slug}`"
                      >{{ post.title }}</router-link
                    >
                  </h2>
                  <router-link
                    v-if="post.category"
                    class="text-sm font-medium uppercase text-blue-500 hover:underline hover:text-blue-700"
                    :to="`/category/${post.category.slug}`"
                    >{{ post.category.name }}</router-link
                  >
                </div>
                <div class="prose max-w-none text-gray-500">
                  {{ trimString(stripHTML(post.content)) }}
                </div>
                <div class="flex items-center mt-4">
                  <img
                    v-if="post.user && post.user.avatar"
                    :src="`/uploads/${post.user.avatar}`"
                    alt="User Avatar"
                    class="w-10 h-10 rounded-full"
                  />
                  <span class="ml-2">{{
                    post.user ? post.user.username : "Unknown"
                  }}</span>
                </div>
              </div>
              <div class="text-base font-medium leading-6">
                <router-link
                  class="text-blue-500 hover:underline hover:text-blue-700"
                  :to="`/post/${post.slug}`"
                >
                  Читать подробнее →
                </router-link>
              </div>
            </div>
          </div>
        </article>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "PostListComponent",
  props: {
    posts: {
      type: Array,
      required: true,
    },
  },
  computed: {
    publishedPosts() {
      return this.posts.filter((post) => post.isPublished);
    },
  },
  methods: {
    stripHTML(string) {
      return string.replace(/<\/?[^>]+>/gi, " ");
    },
    trimString(string) {
      return string.substring(0, 350) + "...";
    },
    formatDate(x) {
      let date = new Date(x);
      var month = [
        "Январь",
        "Февраль",
        "Март",
        "Апрель",
        "Май",
        "Июнь",
        "Июль",
        "Август",
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь",
      ][date.getMonth()];
      return month + " " + date.getDate() + ", " + date.getFullYear();
    },
  },
};
</script>

<style scoped>
.post-item {
  border: 1px solid #e5e7eb; /* light gray border */
  border-radius: 8px; /* rounded corners */
  padding: 16px; /* internal padding */
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1); /* subtle shadow */
  transition: box-shadow 0.3s ease-in-out;
}

.post-item:hover {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* slightly more prominent shadow on hover */
}
</style>
