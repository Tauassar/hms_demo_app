.<template>
    <div v-if="$route.path !== '/login'" class="navigation-buttons">
        <div class="left-part">
            HMS
        </div>
        <div class="right-part">
            <!-- <router-link to="/products" class="button is-text">
                <i class="fa fa-user-circle"></i><span>Shop</span>
            </router-link> -->
            <!-- <router-link to="/cart" class="button is-text">
                <i class="fa fa-shopping-cart"></i><span>CART</span>
            </router-link> -->

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

            <button @click="logout" class="button is-text">Выйти</button>
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
  position: absolute;
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
</style>