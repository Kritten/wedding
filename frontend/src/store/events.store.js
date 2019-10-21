import baseModule from './base.store';

export const moduleEvents = {
  ...baseModule,
  ...{
    state: {
      arrayEvents: [],
    },
  },
};
