const path = require("path");

module.exports = {
  transpileDependencies: [
    'vuetify',
  ],

  pluginOptions: {
    i18n: {
      locale: 'de',
      fallbackLocale: 'de',
      localeDir: 'locales',
      enableInSFC: false,
    },
  },

  outputDir: path.resolve(__dirname, 'dist_tmp'),
};
