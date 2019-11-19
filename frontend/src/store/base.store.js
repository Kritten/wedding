import cloneDeep from 'lodash-es/cloneDeep';
import localforage from 'localforage';

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
    async setState({ commit }, { objectState, nameState, nameStorage }) {
      commit('setState', {
        objectState,
        nameState,
      });

      if (nameStorage !== undefined) {
        await localforage.setItem(nameStorage, objectState);
      }
    },
  },
};
