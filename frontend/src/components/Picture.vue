<template>
  <div class="container">
    <div class="images-div">
      <v-img class="picture" :src="require(`../assets/images/${image.imageName}`)"/>
    </div>
    <div class="v-btn-actions">
      <div class="positive-button">
        <v-btn color="primary" @click.prevent="updateScore('+')">+</v-btn>
      </div>
      <div class="negative-button">
        <v-btn color="primary" @click.prevent="updateScore('-')">-</v-btn>
      </div>
      <div class="score-div">
        <p class="score">Total Score {{ this.score }}</p>
      </div>
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
      await this.$store.dispatch('updateScore', payload);
    }
  }
}
</script>

<style scoped>
.picture {
  width: 500px;
  height: 400px;
  object-fit: cover;
}

.v-btn-actions {
  display: flex;
  justify-content: center;
}

.positive-button, .negative-button {
  padding-left: 10px;
  margin-top: 10px;
}

.score {
  padding-left: 10px;
  margin-top: 15px;
  font-size: 22px;
  font-weight: bolder;
}
</style>