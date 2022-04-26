.<template>
    <div class="user-profile">
        <div class="profile-heading">
            <i class="fa-solid fa-2x fa-address-card"></i>
            <h1>Профиль</h1>
        </div>
            <doctor-profile v-if="user_data.type==='doctor'" :user_data="user_data"/>
            <patient-profile v-if="user_data.type==='patient'" :user_data="user_data"/>
    </div>
</template>

<script>
import DoctorProfile from './DoctorProfile.vue';
import PatientProfile from './PatientProfile.vue';
import axios from '@/app/store/axios';

export default {
    name: 'Profile',
    data(){
        return{
            user_data: {}
        }
    },
    components: {
        'doctor-profile': DoctorProfile,
        'patient-profile':PatientProfile
    },
    mounted(){
        let dest;
        if(this.$route.fullPath.includes("patient")){
            dest = 'patient';
        }else{
            dest = 'doctor';
        }
        axios.get(`user/${dest}/${this.$route.params.username}`).then((response)=>{
            this.user_data = response.data;
        }).catch((error)=>{
            // eslint-disable-next-line no-console
            console.log(error)
        })
    }
}
</script>

<style scoped lang='scss'>
    .profile-heading{
        display: flex;
        align-items: center;
        margin-bottom: 15px;
        h1{
            margin-left: 10px;
            font-size: 32px;
        }
    }
</style>