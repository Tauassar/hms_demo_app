import axios from '../../axios';
import Cookies from 'js-cookie'

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
    return axios.post('user/login/', payload).then((response) => {
      if(response.data){
        let token = response.data['sessionid'];
        Cookies.set('sessionid', token);
        localStorage.setItem("token", token);
        commit('SET_TOKEN', token);
        // const {token, success, ...data} = response.data;
        commit('SET_USER_DATA', response.data);
        commit('LOGIN_SUCCESS');
      }else{
        commit('LOGIN_SUCCESS');
      }
    }).catch((error)=>{
      // eslint-disable-next-line no-console
      console.log(error);
      commit('LOGIN_SUCCESS');
    });
  },
  logout ({ commit }) {
    return axios.get('/user/logout/').then(() => {
      localStorage.removeItem("token");
      sessionStorage.clear();
      commit('SET_TOKEN', null);
    });
  }
}

const getters = {
  token: state => state.token,
  loading: state => state.loading,
  user_name: state => `${state.user_data.first_name} ${state.user_data.last_name}`,
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
