import Vue from 'vue';
import Vuex from 'vuex';
import { moduleApp } from './app.store';

Vue.use(Vuex);

export const store = new Vuex.Store({
  modules: {
    moduleApp,
  },
});
