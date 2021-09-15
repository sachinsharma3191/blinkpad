<template>
  <div class="container">
    <div class="">

    </div>
    <div class="text-button">
      <v-btn color="primary" @click.prevent="updateScore('+')">+</v-btn>
    </div>
    <div class="text-button">
      <v-btn color="primary" @click.prevent="updateScore('-')">-</v-btn>
    </div>
    <div class="text--black">
      {{ this.score }}
    </div>
  </div>
</template>

<script>
export default {
  name: "Image",
  props: {
    Image: {
      type: Object
    }
  },
  mounted() {
    this.score = Image.count
  },
  data() {
    return {
      score: 0
    }
  },
  methods: {
    async updateScore(operation) {
      this.score = operation === "+" ? this.score + 1 : this.score - 1;
      const payload = {
        "count": this.score,
        "imageId": Image.imageId,
        "imageName": Image.imageName
      }
      await this.$store.updateScore(payload);
    }
  }
}
</script>

<style scoped>

</style>