<template>
  <div class="home">
    <div class="flex flex-col place-items-center border-b-2">
      <!-- Featured Image and title -->
      <img
        :src="'/uploads/' + this.postBySlug.featuredImage"
        class="w-full my-5"
      />
      <h1 class="text-center text-5xl font-extrabold mb-5">
        {{ this.postBySlug.title }}
      </h1>
      <p class="text-gray-500 text-lg mb-2">
        {{ formatDate(this.postBySlug.createdAt) }} - От
        {{ this.postBySlug.user.username }}
      </p>
    </div>

    <!-- Tags -->
    <div class="flex flex-wrap my-4">
      <div class="mr-5 text-sm font-medium">Теги:</div>
      <router-link
        v-for="tag in this.postBySlug.tag"
        :key="tag.name"
        class="mr-5 text-sm font-medium uppercase text-teal-500 hover:underline hover:text-teal-700"
        :to="`/tag/${tag.slug}`"
        >{{ tag.name }}</router-link
      >
    </div>

    <!-- Main content -->
    <div class="py-5 font-serif space-y-4">
      <div v-html="this.postBySlug.content"></div>
    </div>

    <!-- Like, Comment and Share -->
    <div
      class="flex flex-wrap py-4 space-x-8 justify-center items-center text-xl"
    >
      <div v-if="this.liked === true" @click="this.updateLike()">
        <i class="fa-solid fa-thumbs-up">
          <span class="font-sans font-semibold ml-1">{{
            this.numberOfLikes
          }}</span>
        </i>
      </div>
      <div v-else @click="this.updateLike()">
        <i class="fa-regular fa-thumbs-up">
          <span class="font-sans font-semibold ml-1">{{
            this.numberOfLikes
          }}</span>
        </i>
      </div>
      <div @click="this.toggleCommentSection()">
        <i class="fa-regular fa-comment-dots"
          ><span class="font-sans font-semibold ml-1">{{
            this.numberOfApprovedComments
          }}</span></i
        >
      </div>
      <div @click="copyLinkToClipboard">
        <i class="fa-solid fa-share-nodes"></i>
      </div>
    </div>

    <!-- Tooltip -->
    <div v-if="showTooltip" class="tooltip">
      Ссылка скопирована!
    </div>

    <!-- Comment Section -->
    <!-- Pass the approved comments and the post id to the comment component -->
    <comment-section-component
      v-if="this.approvedComments && this.showComment"
      :comments="this.approvedComments"
      :postID="this.postBySlug.id"
      :userID="this.userID"
    ></comment-section-component>
  </div>
</template>

<script>
import { POST_BY_SLUG } from "@/queries";
import CommentSectionComponent from "@/components/CommentSection.vue";
import { UPDATE_POST_LIKE } from "@/mutations";

export default {
  name: "PostView",

  components: { CommentSectionComponent },

  data() {
    return {
      postBySlug: null,
      comments: null,
      liked: false,
      numberOfLikes: 0,
      userID: null,
      showComment: false,
      showTooltip: false,
    };
  },

  computed: {
    // Filters out the unapproved comments
    approvedComments() {
      return this.comments.filter((comment) => comment.isApproved);
    },
    numberOfApprovedComments() {
      return Object.keys(this.approvedComments).length;
    },
  },

  async created() {
    // Get the post before the instance is mounted
    const post = await this.$apollo.query({
      query: POST_BY_SLUG,
      variables: {
        slug: this.$route.params.slug,
      },
    });
    this.postBySlug = post.data.postBySlug;
    this.comments = post.data.postBySlug.commentSet;

    // Check if the current user has liked the post
    // Get the current user id
    this.userID = JSON.parse(localStorage.getItem("user")).id;

    // Find if the current user has liked the post
    let likedUsers = this.postBySlug.likes;

    for (let likedUser in likedUsers) {
      if (likedUsers[likedUser].id === this.userID) {
        this.liked = true;
      }
    }

    // Get the number of likes
    this.numberOfLikes = parseInt(this.postBySlug.numberOfLikes);
  },

  methods: {
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
    updateLike() {
      if (this.liked === true) {
        this.numberOfLikes = this.numberOfLikes - 1;
      } else {
        this.numberOfLikes = this.numberOfLikes + 1;
      }
      this.liked = !this.liked;

      this.$apollo.mutate({
        mutation: UPDATE_POST_LIKE,
        variables: {
          postID: this.postBySlug.id,
          userID: this.userID,
        },
      });
    },
    toggleCommentSection() {
      this.showComment = !this.showComment;
    },
    copyLinkToClipboard() {
      const url = window.location.href;
      navigator.clipboard.writeText(url).then(
        () => {
          this.showTooltip = true;
          setTimeout(() => {
            this.showTooltip = false;
          }, 2000);
        },
        (err) => {
          console.error('Ошибка копирования: ', err);
        }
      );
    },
  },
};
</script>

<style scoped>
.tooltip {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 14px;
  z-index: 1000;
}
</style>
