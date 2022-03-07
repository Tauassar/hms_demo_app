.<template>
    <div class="flex-container">
        <div class="profile">
            <i class="fa-solid fa-3x fa-circle-user"></i>
            <div class="profile-text">
                <p class="profile-username">
                    Шамелов Т.Ж
                </p>
                <p class="profile-position">
                    Доктор педиатор общей категории
                </p>
            </div>
        </div>
        <div class="buttons">
            <div v-for="(button, index) in buttons" :key="index" class="button-container">
                <sidebar-button :title='button.title'>
                    <i v-if="button.icon" :class="button.icon"></i>
                    <i v-else class="fa-solid fa-arrow-up-right-from-square"></i>
                </sidebar-button>
            </div>
        </div>
    </div>
</template>

<script>
import Button from './BarButton.vue';

export default {
    name: 'SideBar',
    data() {
        return {
            buttons: [
                {
                    title: 'Главная Страница',
                    link: ''
                },
                {
                    title: 'Департаменты',
                    link: '',
                    icon: 'fa-solid fa-building-columns'
                },
                {
                    title: 'Врачи',
                    link: '',
                    icon: 'fa-solid fa-address-card'
                },
                {
                    title: 'Пациенты',
                    link: ''
                },
                {
                    title: 'Записи',
                    link: ''
                },
                {
                    title: 'Настройки',
                    link: ''
                },
                {
                    title: 'Профиль',
                    link: ''
                },
            ]
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
    color: lightblue;
}
.profile-position{
    color: grey;
    font-size: 12px;
}
</style>