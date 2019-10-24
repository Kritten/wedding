import '@fortawesome/fontawesome-free/css/all.css';
import Vue from 'vue';
import Vuelidate from 'vuelidate';
import App from './App';
import { router } from './router';
import { store } from './store/vuex';
import vuetify from './vuetify';
import i18n from './i18n';

import { Icon } from 'leaflet';
import 'leaflet/dist/leaflet.css';

delete Icon.Default.prototype._getIconUrl;

Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});


Vue.use(Vuelidate);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  i18n,
  render: h => h(App),
}).$mount('#app');
