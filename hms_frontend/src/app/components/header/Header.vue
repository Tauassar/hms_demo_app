.<template>
    <div v-if="$route.path !== '/login'" class="navigation-buttons">
        <router-link to="/">
            <div class="left-part">
                <img  class="header-logo" :src="require('@/app/assets/hms_logo.png')" alt="">
            </div>
        </router-link>
        <div class="right-part">
            <div class="dropdown" @click="toggleDropdown" :class="{'is-active': dropdownActive}">
            <div class="dropdown-trigger">
                <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                <span>Рус</span>
                <span class="icon is-small">
                    <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
                </button>
            </div>
            <div class="dropdown-menu" id="dropdown-menu" role="menu">
                <div class="dropdown-content">
                <a href="#" class="dropdown-item">
                    Eng
                </a>
                </div>
            </div>
            </div>
            <!-- <router-link to="/" class="button is-text">
                <span>{{user_name}}</span>
            </router-link> -->
            <button @click="logout" class="button is-white">Выйти</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Header',
    data() {
        return {
            dropdownActive: false,
        }
    },
    methods: {
        toggleDropdown(){
            this.dropdownActive = !this.dropdownActive
        },
        logout() {
        this.$store.dispatch("logout").then(() => {
            this.$router.push("/login")
        });
        },
    }
}
</script>

<style scoped lang='scss'>
.navigation-buttons {
  top: 0;
  left: 0;
  width: 100%;
  z-index: 99;
  background-color: #2C3E4A;
  height: 50px;
  padding: 0 30px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.left-part{
    color: white;
}

.navigation-buttons .button {
  margin: 0 2px;
}

.is-text{
    text-decoration: none;
    color: white;
}

.navigation-buttons .button .fa {
    padding-right: 5px;
}
.dropdown-menu{
    min-width: 0;
}
.left-part{
    display: flex;
    align-items: center;
}
.header-logo{
    margin: 0 auto;
    width: 75px;
}
</style>