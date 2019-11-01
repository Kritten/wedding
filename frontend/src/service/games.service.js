import { ServiceEndpoint } from './endpoint.service';
import { store } from '../store/vuex';

class ClassServiceGames {
  async loadGames() {
    const response = await ServiceEndpoint.makeRequest({
      url: {
        path: store.state.moduleApp.objectUrls.games,
      },
      method: 'get',
      params: {
        page: 1,
        page_size: 10,
        sort_by: 'title',
        descending: false,
      },
    });

    store.commit('moduleGames/setState', {
      nameState: 'arrayGames',
      objectState: response.data.data,
    });
  }
}
export const ServiceGames = new ClassServiceGames();
