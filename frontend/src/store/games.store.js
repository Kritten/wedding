import baseModule from './base.store';

export const moduleGames = {
  ...baseModule,
  ...{
    state: {
      arrayGames: [],
      countGames: -1,
      countGamesTotal: -1,
    },
  },
};
