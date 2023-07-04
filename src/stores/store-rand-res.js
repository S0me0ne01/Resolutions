import { defineStore } from "pinia";
import axios from "axios";

export const useRandResStore = defineStore("res", {
  state: () => ({
    resolution: "",
    loaded: false,
  }),
  getters: {
    getResolution() {
      return this.resolution;
    },
    getLoaded() {
      return this.loaded;
    },
  },
  actions: {
    async fetchResolution() {
      try {
        const response = await axios.get("http://localhost:8000/random/");
        this.resolution = response.data;
      } catch (error) {
        console.error("Error fetching resolution:", error);
        throw error;
      }
    },
    async setLoaded() {
      this.loaded = !this.loaded;
    },
  },
});
