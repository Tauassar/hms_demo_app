import axios from '@/app/store/axios';

const state = {
    doctor_list: [],
    loading_doctors: false
}

const mutations = {
  SET_DOCTORS_LIST (state, doctor_list) {
    state.doctor_list = doctor_list;
  },
  LOADING_PENDING (state) {
    state.loading_doctors = true;
  },
  LOADING_SUCCESS (state) {
    state.loading_doctors = false;
  },
}

const actions = {
    get_doctor_list ({ commit }) {
        commit('LOADING_PENDING');
        return axios.get('/user/doctor/').then((response) => {
        let data = response.data;
        if(data){
            commit('SET_DOCTORS_LIST', response.data);
            commit('LOADING_SUCCESS');
            // eslint-disable-next-line no-console
            console.log(response.data);
        }else{
            commit('LOADING_SUCCESS');
        }
        });
  },
}

const getters = {
  doctor_list: state => state.doctor_list,
  loading_doctors: state => state.loading_doctors,
}

const doctorsModule = {
    state,
    mutations,
    actions,
    getters
}

export default doctorsModule;
