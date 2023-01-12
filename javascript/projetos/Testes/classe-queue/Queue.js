class Queue {
  constructor() {
    this.data = [];
  }
  enqueue(item) {
    this.data.push(item);
  }
  dequeue() {
    const item = this.data.shift();
    return item;
  }
}

module.exports = Queue;
