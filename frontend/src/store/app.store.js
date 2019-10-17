import baseModule from './base.store';

export const moduleApp = {
  ...baseModule,
  ...{
    state: {
      version_api: null,
    },
    actions: {
      async init({ commit }, config) {
        commit('setState', config.version);

      // commit('moduleAssignments/setUrls', config.paths, { root: true });
      },
    },
  },
};
