<template>
  <div class="flex flex-col my-4 py-4 space-y-10 border-t-2">
    <p class="font-bold text-2xl">Комментарии:</p>

    <!-- If the user is not authenticated -->
    <div v-if="!user.isAuthenticated">
      Вам нужно
      <router-link
        to="/SignIn"
        class="text-blue-500 hover:underline hover:text-blue-700"
        >авторизоваться</router-link
      >
      перед тем как вы сможете комментировать.
    </div>

    <!-- If the user is authenticated -->
    <div v-else>
      <form @submit.prevent="submitComment">
        <textarea
          type="text"
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-300 focus:ring-opacity-50"
          rows="5"
          v-model="commentContent"
        ></textarea>

        <button
          type="submit"
          class="mt-4 w-full bg-blue-500 hover:bg-blue-700 hover:text-blue-100 focus:ring focus:ring-blue-100 text-white py-2 rounded-md text-lg tracking-wide"
        >
          Оставить комментарий
        </button>
      </form>

      <!-- Add this block to refresh the page -->
      <div v-if="commentSubmitSuccess">
        <p>Комментарий публикуется...</p>
    </div>

    </div>

    <!-- List all comments -->
    <comment-single
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
      :userID="userID"
    >
    </comment-single>
  </div>
</template>

<script>
import { SUBMIT_COMMENT } from "@/mutations";
import CommentSingle from "@/components/CommentSingle.vue";
import { useUserStore } from "@/stores/user";

export default {
  components: { CommentSingle },
  name: "CommentSectionComponent",

  setup() {
    const userStore = useUserStore();
    return { userStore };
  },

  data() {
    return {
      commentContent: "",
      commentSubmitSuccess: false,
      user: {
        isAuthenticated: false,
        token: this.userStore.getToken || "",
        info: this.userStore.getUser || {},
      },
    };
  },
  props: {
    comments: {
      type: Array,
      required: true,
    },
    postID: {
      type: String,
      required: true,
    },
    userID: {
      type: String,
      required: true,
    },
  },
  async created() {
    if (this.user.token) {
      this.user.isAuthenticated = true;
    }
  },
  methods: {
    submitComment() {
      if (this.commentContent !== "") {
        this.$apollo
          .mutate({
            mutation: SUBMIT_COMMENT,
            variables: {
              content: this.commentContent,
              userID: this.userID,
              postID: this.postID,
            },
          })
          .then(() => {
            this.commentSubmitSuccess = true;
            location.reload();
            this.commentContent = "";
          });
      }
    },
  },
};
</script>