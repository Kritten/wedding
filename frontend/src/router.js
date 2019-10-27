import Vue from 'vue';
import Router from 'vue-router';
import LoginView from './views/login.view';
import AppView from './views/app/app.view';
import DashboardView from './views/app/dashboard.view';
import EventsView from './views/app/events.view';
import ContactView from './views/app/contact.view';
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
        {
          path: 'events',
          name: 'events',
          component: EventsView,

        },
        {
          path: 'contact',
          name: 'contact',
          component: ContactView,

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
