import { defineStore } from "pinia";
import axios from "axios";

export const useTableStore = defineStore("table", {
  state: () => ({
    resolutions: [],
    loaded: false,
  }),
  getters: {
    getResolutions() {
      return this.resolutions;
    },
    getTableLoaded() {
      return this.loaded;
    },
  },
  actions: {
    async fetchResolutions() {
      try {
        const response = await axios.get("http://localhost:8000");
        this.resolutions = response.data;
      } catch (error) {
        console.error("Error fetching resolutions:", error);
        throw error;
      }
    },
    async setTableLoaded() {
      this.loaded = !this.loaded;
    },
  },
});
