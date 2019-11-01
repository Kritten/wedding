import baseModule from './base.store';

export const moduleGames = {
  ...baseModule,
  ...{
    state: {
      arrayGames: [],
    },
  },
};
