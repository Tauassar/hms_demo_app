import Vue from 'vue';
import Vuex from 'vuex';
import departments from './modules/departments';
import appointments from './modules/appointments';
import patients from './modules/patients';
import login from './modules/login';
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState({
      storage: window.sessionStorage,
  })],
  modules: {
    appointments,
    login,
    departments,
    patients
  }
});
