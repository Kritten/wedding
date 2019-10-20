import baseModule from './base.store';

export const moduleApp = {
  ...baseModule,
  ...{
    state: {
      versionApi: null,
      isInitialized: false,
      isLoggedIn: false,
    },
    actions: {
      // async init({ commit }, config) {
      //   // commit('setState', config.version);
      //
      // // commit('moduleAssignments/setUrls', config.paths, { root: true });
      // },
    },
  },
};
