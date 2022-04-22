<template>
    <div class="main-table is-fullwidth">
        <table class="table is-narrow is-fullwidth">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Пациент</th>
                    <th style="width: 115px">Медицинский статус</th>
                    <th>Группа крови</th>
                    <th>Описание</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(patient, index) in PaginatedPatients" :key="index">
                    <th>{{patient.id}}</th>
                    <th>{{`${patient.first_name} ${patient.last_name}`}}</th>
                    <th>{{medical_status(patient.medical_status).status}}</th>
                    <th>{{medical_status(patient.medical_status).blood_group}}</th>
                    <th>{{patient.description}}</th>
                </tr>
            </tbody>
        </table>
        <div class="pagination">
            <pagination
                v-model='currentPage'
                :maxPage='patient_list.length/paginatedPatientsCount+1'
                prevText='Предыдущая страница'
                nextText='Следующая страница'
            />
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
import Paginate from '@/app/components/utils/pagination.vue'

export default {
    name: 'MainPageFilter',
    components: {
        'pagination': Paginate,
    },
    data() {
        return {
            currentPage: 1,
            paginatedPatientsCount: 7,
            patientData: []
        }
    },
    computed: {
        PaginatedPatients(){
            return this.patient_list.slice(
                (this.currentPage-1)*this.paginatedPatientsCount, 
                this.currentPage*this.paginatedPatientsCount
                )
        },
        ...mapGetters([
            'loading_patients',
            'patient_list'
        ]),
    },
    methods:{
        medical_status(status){
            if(status!=null)
                return status
            return { status: "Данные отсутствуют", blood_group: "Данные отсутствуют" }
        },
    },
    created() {
            this.$store.dispatch("get_patient_list")
    },
}
</script>

<style>
    .table{
        border: 1px solid #DBDBDB;
    }
</style>