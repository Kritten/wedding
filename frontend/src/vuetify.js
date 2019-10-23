import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import colors from 'vuetify/lib/util/colors';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'fa',
  },
  theme: {
    themes: {
      light: {
        primary: colors.indigo.darken4,
        secondary: colors.yellow.accent4,
        // background: colors.grey.lighten3,
      },
    },
  },
});
