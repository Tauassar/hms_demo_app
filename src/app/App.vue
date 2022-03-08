<template>
  <div id="app">
    <custom-header class="header"/>
    <sidebar class="sidebar" v-if="$route.path !== '/login'"/>
    <div 
      class="container"
      :class="{'main-content':$route.path !== '/login'}">
      <div class="columns">
        <div class="column is-8 column--align-center">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import SideBar from './components/sidebar/Sidebar.vue';
import Header from './components/header/Header.vue';

export default {
  name: 'App',
  components:{
    'sidebar': SideBar,
    'custom-header': Header,
  },
  computed: {
    ...mapGetters([
      'token',
      'cartQuantity'
    ])
  },
  created() {
    const token = localStorage.getItem("token");
    if (token) {
      this.updateInitialState(token);
    }
  },
  watch: {
    token() {
      if (this.token) {
        this.updateInitialState(this.token);
      }
    }
  },
  methods: {
    updateInitialState(token) {
      this.$store.dispatch('getCartItems', token);
      this.$store.dispatch('getProductItems', token);
    }
  }
}
</script>

<style>
html, body {
  height: 100%;
  background: #F2F6FA;
}

#app {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.sidebar, .header{
  position: fixed;
  top: 0;
  left: 0;
}

.main-content{
  margin-left: 300px;
  margin-top: 30px;
  position: absolute;
  top: 50px;
}

.container {
  width: 100%;
}

.column--align-center {
  margin: 0 auto;
}

</style>
