<template>
  <div class="hello">
    <div v-if="loading">
      <v-progress-circular
          :size="50"
          color="primary"
          indeterminate
      ></v-progress-circular>
    </div>
    <div v-else>
      <div>
        <li v-for="image in images" :key="image.imageId">
          <Picture :image="image"/>
        </li>
      </div>
    </div>
  </div>
</template>

<script>
import Picture from './Picture';

export default {
  name: 'Pictures',
  components: {
    Picture
  },
  async mounted() {
    await this.loadImages();
  },
  computed: {
    images() {
      return this.$store.getters.images;
    }
  },
  data() {
    return {
      loading: false
    }
  },
  methods: {
    async loadImages() {
      this.loading = true;
      await this.$store.dispatch("loadImages");
      this.loading = false;
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
