<template>
  <div class="q-pa-md">
    <q-form @submit="submitResolution" class="q-gutter-md" style="max-width: 400px; margin: 0 auto;">
      <q-input dark v-model="title" label="Resolution Title" dense outlined bg-color="black" />
      <q-input dark v-model="rating" label="Rating" type="number" dense outlined bg-color="black" />

      <q-select dark v-model="selectedFormat" :options="formatOptions" label="Format" outlined bg-color="black" />
      <q-select dark v-model="selectedCategory" :options="categoryOptions" label="Category" outlined bg-color="black" />

      <q-btn type="submit" label="Submit" class="q-mt-md" style="background-color: black; color: white;" dense flat />
    </q-form>
  </div>
</template>



<script>
import { defineComponent } from 'vue'
import { useTableStore } from 'src/stores/store-table.js'
const store = useTableStore()

export default {
  data() {
    return {
      title: '',
      rating: 0,
      formatOptions: [],
      categoryOptions: [],
      selectedCategory: '',
      selectedFormat: ''
    };
  },

  mounted() {
    this.$axios.get('http://localhost:8000/formats/')
      .then(response => {
        this.formatOptions = response.data;
      })
      .catch(error => {
        console.error('Error fetching format options:', error);
      });

    this.$axios.get('http://localhost:8000/categories/')
      .then(response => {
        this.categoryOptions = response.data;
      })
      .catch(error => {
        console.error('Error fetching category options:', error);
      });
  },

  methods: {
    async submitResolution() {
      if (!this.title || !this.selectedFormat || !this.selectedCategory) {
        alert('Please fill in all fields');
        return;
      }

      try {
        const response = await this.$axios.post('http://localhost:8000/create/resolution/', {
          title: this.title,
          rating: this.rating,
          format: this.selectedFormat,
          category: this.selectedCategory,
        });

        console.log('Resolution created:', response.data);

        this.title = '';
        this.rating = 0;
        this.selectedFormat = null;
        this.selectedCategory = null;
        store.fetchResolutions();
      } catch (error) {
        alert('Error creating resolution:', error);
      }
    },
  },
};

</script>
