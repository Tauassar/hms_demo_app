<template>
    <div class="main-table is-fullwidth">
        <table class="table is-narrow is-fullwidth">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Пациент</th>
                    <th>Дата записи</th>
                    <th>Время записи</th>
                    <th>Пол</th>
                    <th>Дата рождения</th>
                    <th>Описание</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(patient, index) in PaginatedPatients" :key="index">
                    <th>{{patient.id}}</th>
                    <th>{{patient.name}}</th>
                    <th>{{patient.date}}</th>
                    <th>{{patient.time}}</th>
                    <th>{{patient.sex}}</th>
                    <th>{{patient.birth_date}}</th>
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
            patientData: [
                {
                    name: 'Иван Иванов',
                    date: '13.01.2021',
                    time: '14.30',
                    sex: 'Муж',
                    birth_date: '05.07.1999',
                    description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
                },
                {
                    name: 'Иван Иванов',
                    date: '13.01.2021',
                    time: '14.30',
                    sex: 'Муж',
                    birth_date: '05.07.1999',
                    description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
                },
                {
                    name: 'Иван Иванов',
                    date: '13.01.2021',
                    time: '14.30',
                    sex: 'Муж',
                    birth_date: '05.07.1999',
                    description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
                },
                {
                    name: 'Иван Иванов',
                    date: '13.01.2021',
                    time: '14.30',
                    sex: 'Муж',
                    birth_date: '05.07.1999',
                    description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
                },
                {
                    name: 'Иван Иванов',
                    date: '13.01.2021',
                    time: '14.30',
                    sex: 'Муж',
                    birth_date: '05.07.1999',
                    description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
                },
                {
                    name: 'Иван Иванов',
                    date: '13.01.2021',
                    time: '14.30',
                    sex: 'Муж',
                    birth_date: '05.07.1999',
                    description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
                },
                {
                    name: 'Иван Иванов',
                    date: '13.01.2021',
                    time: '14.30',
                    sex: 'Муж',
                    birth_date: '05.07.1999',
                    description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
                },
                {
                    name: 'Иван Иванов',
                    date: '13.01.2021',
                    time: '14.30',
                    sex: 'Муж',
                    birth_date: '05.07.1999',
                    description: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
                },
            ]
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

<style>
    .table{
        border: 1px solid #DBDBDB;
    }
</style>