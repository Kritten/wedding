import localforage from 'localforage';
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

        const hasSeenIntroduction = await localforage.getItem('hasSeenIntroduction');
        commit('moduleGames/setState', {
          nameState: 'hasSeenIntroduction',
          objectState: typeof hasSeenIntroduction !== 'boolean' ? false : hasSeenIntroduction,
        }, { root: true });

        commit('moduleGames/setState', {
          nameState: 'countGamesTotal',
          objectState: config.count_games_total,
        }, { root: true });

        commit('moduleGames/setState', {
          nameState: 'arrayGenres',
          objectState: config.genres,
        }, { root: true });

        commit('moduleGames/setState', {
          nameState: 'arrayMoods',
          objectState: config.moods,
        }, { root: true });

        commit('moduleGames/setState', {
          nameState: 'arrayTypes',
          objectState: config.types,
        }, { root: true });

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
