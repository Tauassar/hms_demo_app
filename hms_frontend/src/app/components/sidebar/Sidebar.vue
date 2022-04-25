.<template>
    <div class="flex-container">
        <router-link to='profile'>
            <div class="profile">
                <i class="fa-solid fa-3x fa-circle-user"></i>
                <div class="profile-text">
                    <p class="profile-username">
                        {{user_name}}
                    </p>
                    <p v-if="user_type=='doctor'" class="profile-position">
                        {{user_data.position}}
                    </p>
                </div>
            </div>
        </router-link>
        <div class="buttons">
            <div v-for="(button, index) in buttons" :key="index" class="button-container">
                <sidebar-button v-if="isButtonRendered(button.title)" :title='button.title' :link='button.link'>
                    <i v-if="button.icon" :class="button.icon"></i>
                    <i v-else class="fa-solid fa-arrow-up-right-from-square"></i>
                </sidebar-button>
            </div>
        </div>
    </div>
</template>

<script>
import Button from './BarButton.vue';
import { mapGetters } from 'vuex';

export default {
    name: 'SideBar',
    data() {
        return {
            buttons: [
                {
                    title: 'Главная Страница',
                    link: '/departments'
                },
                {
                    title: 'Департаменты',
                    link: '/departments',
                    icon: 'fa-solid fa-building-columns'
                },
                {
                    title: 'Врачи',
                    link: '/doctors',
                    icon: 'fa-solid fa-address-card'
                },
                {
                    title: 'Пациенты',
                    link: '/patients'
                },
                {
                    title: 'Записи',
                    link: '/appointments'
                },
                {
                    title: 'Настройки',
                    link: ''
                },
                {
                    title: 'Профиль',
                    link: '/profile'
                },
            ]
        }
    },
    computed: {
        ...mapGetters([
            'user_name',
            'user_type',
            'user_data'
        ]),
    },
    methods:{
        isButtonRendered(title){
            if(title==='Записи') return this.user_type=='doctor';
            return true
        }
    },
    components: {
        'sidebar-button': Button
    }
}
</script>

<style scoped lang='scss'>
.flex-container{
    width: 300px;
    height: 100%;
    background-color: white;
    padding-top: 50px;
}
.profile{
    padding: 20px;
    display: flex;
    height: 130px;
    align-items: center;
}
.profile-text{
    margin-left: 20px;
    color: #82A5BB;
}
.profile-position{
    color: grey;
    font-size: 12px;
}
</style>