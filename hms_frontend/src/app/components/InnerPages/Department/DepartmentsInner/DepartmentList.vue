.<template>
    <div class="list-rapper">
        <card-item v-for="profile in profiles" :profile="profile" :key="profile.id"/>
    </div>
</template>

<script>
import DepartmentCardItem from './DepartmentCard.vue'
import axios from 'axios';

export default {
    name: "CardioDepartment",
    data(){
        return {
            loading: false,
            profiles: []
        }
    },
    created(){
            this.loading = true;
            let route = this.$route.path=='/department/surgery' ? 'surgery':'cardio';
            axios.get(`/api/department/${route}?token=${localStorage.getItem('token')}`).then((response) => {
            let data = response.data;
            this.profiles = data
        })
        .then(
            this.loading = false
        );
    },
    components:{
        'card-item': DepartmentCardItem,
    }
}
</script>

<style scoped lang='scss'>
    .list-rapper{
        padding: 20px 10px;
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;
    }
</style>