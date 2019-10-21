import { ServiceEndpoint } from './endpoint.service';
import { store } from '../store/vuex';

class ClassServiceEvents {
  async loadEvents() {
    const response = await ServiceEndpoint.makeRequest({
      url: {
        path: store.state.moduleApp.objectUrls.events,
      },
      method: 'get',
      params: {
        sort_by: 'datetime',
        descending: false,
      },
    });

    store.commit('moduleEvents/setState', {
      nameState: 'arrayEvents',
      objectState: response.data.data,
    });
  }
}
export const ServiceEvents = new ClassServiceEvents();
