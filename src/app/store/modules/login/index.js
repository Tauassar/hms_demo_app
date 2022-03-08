import axios from 'axios';

const state = {
  token: null,
  user_data: {},
  loading: false
}

const mutations = {
  SET_TOKEN (state, token) {
    state.token = token;
  },
  LOGIN_PENDING (state) {
    state.loading = true;
  },
  LOGIN_SUCCESS (state) {
    state.loading = false;
  },
  SET_USER_DATA (state, data) {
    state.user_data = data;
  },
}

const actions = {
  login ({ commit }, payload) {
    commit('LOGIN_PENDING');
    return axios.post('/api/login', payload).then((response) => {
      let token = response.data.token;
      if(token){
        localStorage.setItem("token", response.data.token);
        commit('SET_TOKEN', response.data.token);
        const {token, success, ...data} = response.data; 
        commit('SET_USER_DATA', data);
        commit('LOGIN_SUCCESS');
      }else{
        commit('LOGIN_SUCCESS');
      }
    });
  },
  logout ({ commit }) {
    return new Promise((resolve) => {
      localStorage.removeItem("token");
      sessionStorage.clear();
      commit('SET_TOKEN', null);
      resolve();
    });
  }
}

const getters = {
  token: state => state.token,
  loading: state => state.loading,
  user_name: state => state.user_data.name,
  user_type: state => state.user_data.type,
  user_data: state => state.user_data
}

const loginModule = {
  state,
  mutations,
  actions,
  getters
}

export default loginModule;
