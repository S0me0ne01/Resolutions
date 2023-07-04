<template>
  <q-card dark class="my-card">
    <q-card-section>
      <p style="font-size: 20px;" v-if="isLoading">
        Loading...
      </p>
      <p style="font-size: 20px;" v-else>
        {{ res }}
      </p>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  data() {
    return {
      isLoading: true,
      res: ''
    }
  },

  created() {
    this.fetchData()
  },

  methods: {
    async fetchData() {
      try {
        const response = await this.$axios.get('http://localhost:8000/random/')
        this.res = response.data
      } catch (error) {
        console.error('Error fetching data:', error)
      } finally {
        this.isLoading = false
      }
    }
  }
};
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 250px
</style>
