import baseModule from './base.store';

export const moduleApp = {
  ...baseModule,
  ...{
    state: {
      versionApi: null,
      isInitialized: false,
      isLoggedIn: false,
      objectUrls: {},
    },
    actions: {
      async init({ commit }, config) {
        commit('setState', config.version);

        commit('setState', {
          nameState: 'objectUrls',
          objectState: config.paths,
        });
      },
    },
  },
};
