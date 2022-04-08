import Vue from 'vue';
import Vuex from 'vuex';
import product from './modules/product';
import cart from './modules/cart';
import departments from './modules/departments';
import appointments from './modules/appointments';
import login from './modules/login';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState({
      storage: window.sessionStorage,
  })],
  modules: {
    appointments,
    product,
    cart,
    login,
    departments
  }
});
