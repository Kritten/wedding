class QueueClass {
  constructor() {
    this.listeners = {};
  }

  notify(type, payload) {
    if (this.listeners[type] !== undefined) {
      this.listeners[type].forEach((callback) => {
        callback(payload);
      });
    }
  }

  listen(type, callback) {
    if (this.listeners[type] === undefined) {
      this.listeners[type] = [];
    }

    this.listeners[type].push(callback);
  }
}


export const Queue = new QueueClass();
