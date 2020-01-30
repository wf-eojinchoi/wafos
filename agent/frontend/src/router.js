import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Language from './views/Language.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'language',
      component: Language
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/washer',
      name: 'washer',
      component: () =>
        import(/* webpackChunkName: "washer" */ './views/washer/Washer.vue')
    },
    {
      path: '/dryer',
      name: 'dryer',
      component: () =>
        import(/* webpackChunkName: "dryer" */ './views/dryer/Dryer.vue')
    },
    {
      path: '/shoes-washer',
      name: 'shoes-washer',
      component: () =>
        import(/* webpackChunkName: "shoes-washer" */ './views/shoes-washer/ShoesWasher.vue')
    },
    {
      path: '/shoes-dryer',
      name: 'shoes-dryer',
      component: () =>
        import(/* webpackChunkName: "shoes-dryer" */ './views/shoes-dryer/ShoesDryer.vue')
    },
    {
      path: '/styler',
      name: 'styler',
      component: () =>
        import(/* webpackChunkName: "styler" */ './views/styler/Styler.vue')
    },
    {
      path: '/airconditioner',
      name: 'airconditioner',
      component: () =>
        import(/* webpackChunkName: "airconditioner" */ './views/airconditioner/Airconditioner.vue')
    },
    {
      path: '/supplies',
      name: 'supplies',
      component: () =>
        import(/* webpackChunkName: "supplies" */ './views/supplies/Supplies.vue')
    },
    {
      path: '/login/phone',
      name: 'login-phone',
      component: () =>
        import(/* webpackChunkName: "login-phone" */ './views/login/Phone.vue')
    },
    {
      path: '/login/password',
      name: 'login-password',
      component: () =>
        import(/* webpackChunkName: "login-password" */ './views/login/Password.vue')
    },
    {
      path: '/register/phone',
      name: 'register-phone',
      component: () =>
        import(/* webpackChunkName: "register-phone" */ './views/register/Phone.vue')
    },
    {
      path: '/register/password',
      name: 'register-password',
      component: () =>
        import(/* webpackChunkName: "register-password" */ './views/register/Password.vue')
    },
    {
      path: '/info',
      name: 'info',
      component: () =>
        import(/* webpackChunkName: "mainpage" */ './views/Info.vue')
    },
    {
      path: '/init',
      name: 'init',
      component: () =>
        import(/* webpackChunkName: "mainpage" */ './views/Init.vue')
    },
    {
      path: '/build-error',
      name: 'build-error',
      component: () =>
        import(/* webpackChunkName: "mainpage" */ './views/BuildError.vue')
    },
    {
      path: '/build-error-expired',
      name: 'build-error-expired',
      component: () =>
        import(/* webpackChunkName: "mainpage" */ './views/BuildErrorExpired.vue')
    },
    {
      path: '/history',
      name: 'history',
      component: () =>
        import(/* webpackChunkName: "mainpage" */ './views/History.vue')
    },
    {
      path: '/charge',
      name: 'charge',
      component: () =>
        import(/* webpackChunkName: "mainpage" */ './views/Charge.vue')
    },
    {
      path: '/first',
      name: 'first',
      component: () =>
        import(/* webpackChunkName: "mainpage" */ './views/FirstPage.vue')
    }
  ]
})
