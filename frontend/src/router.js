import Vue from 'vue';
import Router from 'vue-router';
import LoginView from './views/login.view';
import AppView from './views/app/app.view';
import DashboardView from './views/app/dashboard.view';
import { Queue } from './queue';

Vue.use(Router);

export const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/',
      component: AppView,
      children: [
        {
          path: '',
          name: 'dashboard',
          component: DashboardView,

        },
      ],
    },
  ],
});

Queue.listen('router', (payload) => {
  if (payload.name !== router.currentRoute.name) {
    router.push(payload);
  }
});
