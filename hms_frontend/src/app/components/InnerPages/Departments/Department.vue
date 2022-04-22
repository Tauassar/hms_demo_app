.<template>
    <div class="department-container">
        <h1 class="container-name">
            Департаменты
        </h1>
        <div class="departments-list">
            <department-item 
                v-for="(department, index) in department_list"
                :key="index"
                :title="department.title"
                :link="department.link"
                :subtitle="department.subtitle"
                :id="department.id"
            />
        </div>
    </div>
</template>

<script>
import DepartmentItem from './DepartmentItem.vue';
import { mapGetters } from 'vuex';

export default {
    name: 'Department',
    components: {
        'department-item': DepartmentItem,
    },
    computed: {
        ...mapGetters([
        'department_list'
        ])
    },
    created() {
        // get_department_list() {
            this.$store.dispatch("get_department_list").then(() => {
                this.$router.push({ path: '/' });
            });
        // }
    }
}
</script>

<style>
    .container-name{
        font-size: 22px;
        margin-bottom: 10px;
    }
    .departments-list{
        height: 300px;
        display: grid; 
        grid-template-columns: 1fr 1fr 1fr; 
        grid-template-rows: 1fr 1fr; 
        gap: 2px 2px; 
        grid-template-areas: 
            ". . ."
            ". . ."; 
    }
</style>