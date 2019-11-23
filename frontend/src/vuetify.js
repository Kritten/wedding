import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import colors from 'vuetify/lib/util/colors';
import de from 'vuetify/es5/locale/de';

Vue.use(Vuetify);

export default new Vuetify({
  lang: {
    locales: { de },
    current: 'de',
  },
  icons: {
    iconfont: 'fa',
  },
  theme: {
    themes: {
      light: {
        primary: colors.indigo.darken2,
        secondary: '#ffe588',
        accent: '#b9c4ca',
        // primary: colors.indigo.darken4,
        // secondary: colors.yellow.accent4,
        // accent: colors.grey.base,
      },
    },
  },
});
