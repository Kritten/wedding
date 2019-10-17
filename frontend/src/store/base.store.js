import cloneDeep from 'lodash-es/cloneDeep';

export default {
  namespaced: true,
  state: {
  },
  getters: {
  },
  mutations: {
    setState(state, { objectState, nameState }) {
      state[nameState] = cloneDeep(objectState);
    },
  },
  actions: {
    async setState({ commit }, { objectState, nameState }) {
      commit('setState', {
        objectState,
        nameState,
      });
    },
  },
};
