<template>
  <div id="login" class="box has-text-centered">
    <h2 class="title">HMS</h2>
    <div class="flex">
      <i class="fa fa-2x fa-user-circle"></i>
      <input class="input is-primary" type="text" placeholder="ИИН">
    </div>
    <div class="margin-top-medium flex">
      <i class="fa-2x fa-solid fa-lock"></i>
      <input class="input is-primary" type="Password" placeholder="Пароль">
    </div>
    <button @click="login"
      :class="[{'is-loading': loading}, 'button is-primary full-width']">
      Login
    </button>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'Login',
  computed: {
    ...mapGetters([
      'loading',
    ])
  },
  methods: {
    login() {
      this.$store.dispatch("login").then(() => {
        this.$router.push({ path: '/products' });
      });
    }
  }
}
</script>

<style scoped lang="scss">
.box {
  padding: 30px 110px;
}
.margin-top-medium{
  margin: 10px 0 30px 0;
}
.flex{
  display: flex;
  input{
    margin-left: 10px;
  }
  i{
    width: 40px;
  }
}
.full-width{
  width: 100%;
}
</style>
