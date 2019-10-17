import { store } from '../store/vuex';
import {ServiceEndpoint} from './endpoint.service';

class ClassServiceApp {
  async init() {
    ServiceEndpoint.init();

    const response = await ServiceEndpoint.makeRequest({
      url: {
        path: 'config',
      },
      method: 'get',
    });

    console.warn('response', response);
    // store.dispatch('moduleApp/init');
  }
}
export const ServiceApp = new ClassServiceApp();
