import axios from 'axios';

const state = {
  department_list: [],
  loading_departments: false
}

const mutations = {
  SET_DEPARTMENT_LIST (state, department_list) {
    state.department_list = department_list;
  },
  LOADING_PENDING (state) {
    state.loading_departments = true;
  },
  LOADING_SUCCESS (state) {
    state.loading_departments = false;
  },
}

const actions = {
    get_department_list ({ commit }) {
        commit('LOADING_PENDING');
        return axios.get(`/api/departments?token=${localStorage.getItem('token')}`).then((response) => {
        let data = response.data;
        if(data){
            commit('SET_DEPARTMENT_LIST', response.data);
            commit('LOADING_SUCCESS');
            // console.log(response.data);
        }else{
            commit('LOADING_SUCCESS');
        }
        });
  },
}

const getters = {
    department_list: state => state.department_list,
    loading_departments: state => state.loading_departments,
}

const depModule = {
    state,
    mutations,
    actions,
    getters
}

export default depModule;
