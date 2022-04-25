import Vue from 'vue';
import VueRouter from 'vue-router';
import LoginBox from '../components/login/LoginBox.vue';
import NotFound from '../components/NotFound.vue';
import MainPage from '../components/InnerPages/Appointments/MainPage.vue'
import Profile from '../components/InnerPages/Profile/Profile.vue'
import Patients from '../components/InnerPages/Patients/PatientsPage.vue'
import Doctors from '../components/InnerPages/Doctors/DoctorsPage.vue'
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
      path: '/patients',
      component: Patients
    },
    {
      path: '/doctors',
      component: Doctors
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
          path: ':id',
          name: 'department',
          component: DepartmentList,
          props: true,
        },
      ]
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
