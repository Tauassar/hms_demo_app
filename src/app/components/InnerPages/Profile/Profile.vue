.<template>
    <div class="user-profile">
        <div class="profile-heading">
            <i class="fa-solid fa-2x fa-address-card"></i>
            <h1>Профиль</h1>
        </div>
        <doctor-profile v-if="user_data.type==='doctor'"/>
    </div>
</template>

<script>
import DoctorProfile from './DoctorProfile.vue';
import {mapGetters} from 'vuex';

export default {
    name: 'Profile',
    components: {
        'doctor-profile': DoctorProfile
    },
    computed:{
        ...mapGetters([
            'user_data'
        ])
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