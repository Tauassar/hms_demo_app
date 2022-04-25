<template>
    <div class="main-table is-fullwidth">
        <table class="table is-narrow is-fullwidth">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Пациент</th>
                    <th style="width: 115px">Дата записи</th>
                    <th>Время записи</th>
                    <th>Описание</th>
                </tr>
            </thead>
            <tbody>
                <tr @click="$router.push(`/appointments/${patient.id}`)" v-for="(patient, index) in PaginatedPatients" :key="index">
                    <th>{{index+1}}</th>
                    <th>{{patient.patient}}</th>
                    <th>{{patient.date}}</th>
                    <th>{{patient.time_str}}</th>
                    <th>{{patient.description}}</th>
                </tr>
            </tbody>
        </table>
        <div class="pagination">
            <pagination
                v-model='currentPage'
                :maxPage='appointment_list.length/paginatedPatientsCount+1'
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
            return this.appointment_list.slice(
                (this.currentPage-1)*this.paginatedPatientsCount, 
                this.currentPage*this.paginatedPatientsCount
                )
        },
        ...mapGetters([
        'loading_appointments',
        'appointment_list'
        ])
    },
    created() {
        // get_department_list() {
            this.$store.dispatch("get_appointment_list")
        // }
    },
}
</script>

<style lang='scss'>
    .table{
        border: 1px solid #DBDBDB;
        tbody{
            tr{
                cursor: pointer;
                &:hover{
                    background-color: #DBDBDB;
                }
            }
        }
    }
</style>