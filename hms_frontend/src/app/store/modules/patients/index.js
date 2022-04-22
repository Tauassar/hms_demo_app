import axios from '@/app/store/axios';

const state = {
    patient_list: [],
    loading_patients: false
}

const mutations = {
  SET_PATIENTS_LIST (state, patient_list) {
    state.patient_list = patient_list;
  },
  LOADING_PENDING (state) {
    state.loading_patients = true;
  },
  LOADING_SUCCESS (state) {
    state.loading_patients = false;
  },
}

const actions = {
    get_patient_list ({ commit }) {
        commit('LOADING_PENDING');
        return axios.get('/user/patient/').then((response) => {
        let data = response.data;
        if(data){
            commit('SET_PATIENTS_LIST', response.data);
            commit('LOADING_SUCCESS');
            // console.log(response.data);
        }else{
            commit('LOADING_SUCCESS');
        }
        });
  },
}

const getters = {
  patient_list: state => state.patient_list,
  loading_patients: state => state.loading_patients,
}

const patientsModule = {
    state,
    mutations,
    actions,
    getters
}

export default patientsModule;
