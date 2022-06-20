const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const stdin = fs
  .readFileSync(inputPath)
  .toString()
  .split("\n")
  .map((line) => line.trim());

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

class Node {
  constructor(data, prev, next) {
    this.data = data;
    this.prev = prev;
    this.next = next;
  }
}

class Deque {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  pushFront(data) {
    if (this.length === 0) {
      this.head = new Node(data, null, null);
      this.tail = this.head;
    } else {
      const frontNode = this.head;
      this.head = new Node(data, null, frontNode);
      frontNode.prev = this.head;
    }
    this.length += 1;
  }

  pushBack(data) {
    if (this.length === 0) {
      this.head = new Node(data, null, null);
      this.tail = this.head;
    } else {
      const backNode = this.tail;
      this.tail = new Node(data, backNode, null);
      backNode.next = this.tail;
    }
    this.length += 1;
  }

  popFront() {
    let frontNode;
    if (this.length === 0) {
      return -1;
    } else if (this.length === 1) {
      frontNode = this.head;
      this.head = null;
      this.tail = null;
    } else {
      frontNode = this.head;
      this.head = this.head.next;
      this.head.prev = null;
    }
    this.length -= 1;
    return frontNode.data;
  }

  popBack() {
    let backNode;
    if (this.length === 0) {
      return -1;
    } else if (this.length === 1) {
      backNode = this.tail;
      this.head = null;
      this.tail = null;
    } else {
      backNode = this.tail;
      this.tail = this.tail.prev;
      this.tail.next = null;
    }
    this.length -= 1;
    return backNode.data;
  }

  size() {
    return this.length;
  }

  empty() {
    return this.length === 0 ? 1 : 0;
  }

  front() {
    return this.length === 0 ? -1 : this.head.data;
  }

  back() {
    return this.length === 0 ? -1 : this.tail.data;
  }
}

const solution = () => {
  const n = Number(input());
  const deque = new Deque();
  const ans = [];
  for (let i = 0; i < n; i++) {
    const oper = input().split(" ");
    if (oper[0] === "push_front") {
      deque.pushFront(oper[1]);
    } else if (oper[0] === "push_back") {
      deque.pushBack(oper[1]);
    } else if (oper[0] === "pop_front") {
      ans.push(deque.popFront());
    } else if (oper[0] === "pop_back") {
      ans.push(deque.popBack());
    } else if (oper[0] === "size") {
      ans.push(deque.size());
    } else if (oper[0] === "empty") {
      ans.push(deque.empty());
    } else if (oper[0] === "front") {
      ans.push(deque.front());
    } else if (oper[0] === "back") {
      ans.push(deque.back());
    }
  }
  console.log(ans.join("\n"));
};

solution();
