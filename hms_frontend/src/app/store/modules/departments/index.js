import axios from '../../axios'
// import axios from 'axios';

const state = {
  department_list: [],
  loading_departments: false,
  current_department: {}
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
  CURRENT_DEPARTMENT (state, department_obj) {
    state.current_department = department_obj;
  },
}

const actions = {
    get_department_list ({ commit }) {
        commit('LOADING_PENDING');
        return axios.get(`/departments`).then((response) => {
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
  set_current_department ({ commit, state }, id) {
    let obj = state.department_list.find((data)=>{
      return data.id == id
    })
    commit('CURRENT_DEPARTMENT', obj)
  },
}

const getters = {
    department_list: state => state.department_list,
    loading_departments: state => state.loading_departments,
    current_department: state => state.current_department,
}

const depModule = {
    state,
    mutations,
    actions,
    getters
}

export default depModule;
