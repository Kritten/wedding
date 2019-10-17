import { ServiceEndpoint } from './endpoint.service';

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
  }
}
export const ServiceApp = new ClassServiceApp();
