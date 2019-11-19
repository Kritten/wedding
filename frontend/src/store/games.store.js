import baseModule from './base.store';

export const moduleGames = {
  ...baseModule,
  ...{
    state: {
      arrayGames: [],
      countGames: -1,
      countGamesTotal: -1,
      arrayGenres: [],
      arrayMoods: [],
      arrayTypes: [],
      hasSeenIntroduction: false,
    },
  },
};
