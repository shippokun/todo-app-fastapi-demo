import Vue from "vue";
import Vuex from "vuex";
import router from "./router";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    logined: localStorage.getItem("vue-token") ? true : false,
    error: false
  },
  mutations: {
    logined(state, payload) {
      state.logined = true;
    },
    error(state, payload) {
      // main.jsに記述されたGraphQLのグローバルエラーをハンドリングする
      router.push("/login");
    }
  }
});
