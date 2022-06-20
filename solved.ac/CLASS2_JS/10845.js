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
  constructor(prev, next, data) {
    this.prev = prev;
    this.next = next;
    this.data = data;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(data) {
    if (this.length === 0) {
      this.head = new Node(null, null, data);
      this.tail = this.head;
    } else {
      const node = this.tail;
      this.tail = new Node(node, null, data);
      node.next = this.tail;
    }
    this.length += 1;
  }

  pop() {
    let node;
    if (this.length === 0) {
      return -1;
    } else if (this.length === 1) {
      node = this.head;
      this.head = null;
      this.tail = null;
    } else {
      node = this.head;
      this.head = this.head.next;
      this.head.prev = null;
    }
    this.length -= 1;
    return node.data;
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
  const q = new Queue();
  const ans = [];
  for (let i = 0; i < n; i++) {
    const oper = input().split(" ");
    if (oper[0] === "push") {
      q.push(oper[1]);
    } else if (oper[0] === "pop") {
      ans.push(q.pop());
    } else if (oper[0] === "size") {
      ans.push(q.size());
    } else if (oper[0] === "empty") {
      ans.push(q.empty());
    } else if (oper[0] === "front") {
      ans.push(q.front());
    } else if (oper[0] === "back") {
      ans.push(q.back());
    }
  }
  console.log(ans.join("\n"));
};

solution();
