.<template>
    <div class="list-rapper">
        <span v-if="profiles.length==0">К сожалению нету доступных врачей для записи</span>
        <card-item v-for="profile in profiles" :profile="profile" :key="profile.id"/>
    </div>
</template>

<script>
import DepartmentCardItem from './DepartmentCard.vue'
import axios from '@/app/store/axios';

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
            axios.get(`/departments/${this.$route.params.id}`).then((response) => {
            let data = response.data;
            // eslint-disable-next-line no-console
            console.log(data)
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