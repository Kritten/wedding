import Vue from 'vue';
import Vuex from 'vuex';
import { moduleApp } from './app.store';
import { moduleEvents } from './events.store';

Vue.use(Vuex);

export const store = new Vuex.Store({
  modules: {
    moduleApp,
    moduleEvents,
  },
});
