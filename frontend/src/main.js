import Vue from 'vue';
import Vuelidate from 'vuelidate';
import App from './App';
import { router } from './router';
import { store } from './store/vuex';
import vuetify from './plugins/vuetify';
import i18n from './i18n';

Vue.use(Vuelidate);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  i18n,
  render: h => h(App),
}).$mount('#app');
