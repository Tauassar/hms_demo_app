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
    <div v-if="modalIsOpen" @click.self="modalIsOpen=false" class="folder-block">
      <modal-form />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import SideBar from './components/sidebar/Sidebar.vue';
import Header from './components/header/Header.vue';
import ModalForm from './components/InnerPages/Department/DepartmentsInner/ModalForm.vue'


export default {
  name: 'App',
  components:{
    'sidebar': SideBar,
    'custom-header': Header,
    'modal-form': ModalForm
  },
  data(){
      return {
          modalIsOpen: false
      }
  },
  computed: {
    ...mapGetters([
      'token',
    ])
  },
  created() {
    this.$eventHub.$on('open_modal', ()=>{
      this.modalIsOpen = true;
    })
    this.$eventHub.$on('close_modal', ()=>{
      this.modalIsOpen = false;
    })
  },
  beforeDestroy() {
      this.$eventHub.$off('close_modal');
      this.$eventHub.$off('open_modal');
  },
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

.folder-block{
  position: fixed;
  left: 0%;
  width: 0%;
  background-color: rgba(0, 0, 0, 0.274);
  width: 100%;
  height: 100%;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>
