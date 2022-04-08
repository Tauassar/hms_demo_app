import axios from 'axios';

const state = {
    appointment_list: [],
    loading_appointments: false
}

const mutations = {
  SET_APPOINTMENT_LIST (state, appointment_list) {
    state.appointment_list = appointment_list;
  },
  LOADING_PENDING (state) {
    state.loading_appointments = true;
  },
  LOADING_SUCCESS (state) {
    state.loading_appointments = false;
  },
}

const actions = {
    get_appointment_list ({ commit }) {
        commit('LOADING_PENDING');
        return axios.get(`/api/appointments?token=${localStorage.getItem('token')}`).then((response) => {
        let data = response.data;
        if(data){
            commit('SET_APPOINTMENT_LIST', response.data);
            commit('LOADING_SUCCESS');
            // console.log(response.data);
        }else{
            commit('LOADING_SUCCESS');
        }
        });
  },
}

const getters = {
    appointment_list: state => state.appointment_list,
    loading_appointments: state => state.loading_appointments,
}

const appointmentModule = {
    state,
    mutations,
    actions,
    getters
}

export default appointmentModule;
