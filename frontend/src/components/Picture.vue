<template>
  <div class="container">
    <div class="">

    </div>
    <div class="text-button">
      <button color="primary" @click.prevent="updateScore('+')">+</button>
    </div>
    <div class="text-button">
      <button color="primary" @click.prevent="updateScore('-')">-</button>
    </div>
    <div class="text--black">
      {{ this.score }}
    </div>
  </div>
</template>

<script>
export default {
  name: "Picture",
  props: {
    image: {
      type: Object
    }
  },
  mounted() {
    this.score = this.image.count
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
        "imageId": this.image.imageId,
        "imageName": this.image.imageName
      }
      await this.$store.updateScore(payload);
    }
  }
}
</script>

<style scoped>

</style>