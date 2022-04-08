import Vue from 'vue';
import VueRouter from 'vue-router';
import CartList from '../components/cart/CartList.vue';
import ProductList from '../components/product/ProductList.vue';
import ProductItem from '../components/product/ProductItem.vue';
import LoginBox from '../components/login/LoginBox.vue';
import NotFound from '../components/NotFound.vue';
import MainPage from '../components/InnerPages/Appointments/MainPage.vue'
import Profile from '../components/InnerPages/Profile/Profile.vue'
import Departments from '../components/InnerPages/Departments/Department.vue'
import Department from '../components/InnerPages/Department/Department.vue'
import DepartmentList from '../components/InnerPages/Department/DepartmentsInner/DepartmentList.vue'

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/appointments',
      component: MainPage
    },
    {
      path: '/profile',
      component: Profile
    },
    {
      path: '',
      redirect: '/departments'
    },
    {
      path: '/departments',
      component: Departments
    },
    {
      path: '/department/',
      component: Department,
      children: [
        {
          path: 'cardio',
          component: DepartmentList,
        },
        {
          path: 'surgery',
          component: DepartmentList,
        },
      ]
    },
    {
      path: '/products',
      component: ProductList
    },
    {
      path: '/products/:id',
      component: ProductItem,
      props: true,
      beforeEnter: (to, from, next) => {
        const id = to.params.id;
        if (![1, 2, 3, 4].includes(Number(id))) next('/not-found');
        else next();
      }
    },
    {
      path: '/cart',
      component: CartList
    },
    {
      path: '/login',
      component: LoginBox,
      beforeEnter: (to, from, next) => {
        const token = localStorage.getItem("token");
        if (token) next('');
        else next();
      }
    },
    {
      path: '*',
      component: NotFound
    }
  ]
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token");
  if (!token && to.path !== '/login') next('/login');
  else next();
});

export default router;
