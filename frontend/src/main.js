import Vue from "vue";
import App from "./App.vue";
import router from "./router";
// import store from "./store";

// Bootstrap
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

// Apollo
import { ApolloClient } from "apollo-client";
import { setContext } from "apollo-link-context";
import { createHttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";
import VueApollo from "vue-apollo";

Vue.config.productionTip = false;

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueApollo);

// CreateHttpLinkでエンドポイントの指定
const httpLink = createHttpLink({
  uri: "http://localhost:8000/graphql"
});

// ログイン後にBearerを指定したJWT通信が入るので先に記述
// 今回はlocalstrageを用いてtokenを保持する
const authLink = setContext((_, { headers }) => {
  const token = localStorage.getItem("vue_token");
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : ""
    }
  };
});

// ApolloClientの初期化
// linkとmemoryCacheを有効化
const apolloClient = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache()
});

// apolloProviderの設定
// storeへエラー通知を設定するので、storeへのコミットを記述
const apolloProvider = new VueApollo({
  defaultClient: apolloClient
  // errorHandler(error) {
  //   store.commit("erroe");
  // }
});

// Vueの初期化の際にapolloProviderの設定を組み込む
new Vue({
  router,
  apolloProvider,
  render: h => h(App)
}).$mount("#app");
