import baseModule from './base.store';

export const moduleApp = {
  ...baseModule,
  ...{
    state: {
      versionApi: null,
      isInitialized: false,
      isLoggedIn: false,
      objectUrls: {},
      objectUser: null,
      objectSnackbar: null,
    },
    actions: {
      async init({ commit }, config) {
        commit('setState', config.version);

        commit('setState', {
          nameState: 'objectUrls',
          objectState: config.paths,
        });
      },
      openSnackbar({ commit }, objectSnackbar) {
        commit('setState', {
          objectState: objectSnackbar,
          nameState: 'objectSnackbar',
        });
      },
    },
  },
};
