import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import HomePage from '../views/HomePage.vue'
import AmazonList from '../views/AmazonList.vue'
import EbayList from '../views/EbayList.vue'
import YelpList from '../views/YelpList.vue'
import IndexPage from '../views/IndexPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/home',
    name: 'home',
    component: HomePage
  },
  {
    path: '/AmazonList',
    name: 'AmazonList',
    component: AmazonList
  },
  {
    path: '/EbayList',
    name: 'EbayList',
    component: EbayList
  },
  {
    path: '/YelpList',
    name: 'YelpList',
    component: YelpList
  },
  {
    path: '/IndexPage',
    name: 'IndexPage',
    component: IndexPage
  },

  

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
