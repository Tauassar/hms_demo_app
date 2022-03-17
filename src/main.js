import Vue from 'vue';
import App from './app/App.vue';
import router from './app/router';
import store from './app/store/index.js';

Vue.prototype.$eventHub = new Vue();

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
