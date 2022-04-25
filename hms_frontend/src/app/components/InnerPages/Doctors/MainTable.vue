<template>
    <div class="main-table is-fullwidth">
        <table class="table is-narrow is-fullwidth">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Имя</th>
                    <th>Должность</th>
                    <th>Департамент</th>
                    <th>Описание</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(doctor, index) in PaginatedDoctors" :key="index">
                    <th>{{index}}</th>
                    <th>{{`${doctor.first_name} ${doctor.last_name}`}}</th>
                    <th>{{doctor.position}}</th>
                    <th>{{doctor.department_str}}</th>
                    <th>{{doctor.short_description}}</th>
                </tr>
            </tbody>
        </table>
        <div class="pagination">
            <pagination
                v-model='currentPage'
                :maxPage='doctor_list.length/paginatedDoctorsCount+1'
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
            paginatedDoctorsCount: 7,
            doctorData: []
        }
    },
    computed: {
        PaginatedDoctors(){
            return this.doctor_list.slice(
                (this.currentPage-1)*this.paginatedDoctorsCount, 
                this.currentPage*this.paginatedDoctorsCount
                )
        },
        ...mapGetters([
            'loading_doctors',
            'doctor_list'
        ]),
    },
    created() {
            this.$store.dispatch("get_doctor_list")
    },
}
</script>

<style>
    .table{
        border: 1px solid #DBDBDB;
    }
</style>