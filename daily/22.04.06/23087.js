const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : fs.readFileSync("ex.txt").toString()
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

class PriorityQ {
  constructor() {
    this.q = [];
  }

  insert(val) {
    this.q.push(val);
    let index = this.q.length - 1;

    while (index > 0) {
      let parentIndex = parseInt((index - 1) / 2);
      if (this.q[parentIndex][0] <= val[0]) return;
      let temp = this.q[parentIndex];
      this.q[parentIndex] = val;
      this.q[index] = temp;
      index = parentIndex;
    }
  }

  pop() {
    if (this.q.length === 0) return;
    if (this.q.length === 1) return this.q.pop();
    const first = this.q[0];

    this.q[0] = this.q.pop();

    let index = 0;
    while (true) {
      let leftChild = index * 2 + 1;
      let rightChild = index * 2 + 2;
      let temp;
      if (rightChild < this.q.length) {
        if (
          this.q[index][0] >
          Math.min(this.q[leftChild][0], this.q[rightChild][0])
        ) {
          if (this.q[leftChild][0] < this.q[rightChild][0]) {
            temp = this.q[leftChild];
            this.q[leftChild] = this.q[index];
            this.q[index] = temp;
            index = leftChild;
          } else {
            temp = this.q[rightChild];
            this.q[rightChild] = this.q[index];
            this.q[index] = temp;
            index = rightChild;
          }
        } else {
          break;
        }
      } else if (leftChild < this.q.length) {
        if (this.q[index][0] > this.q[leftChild][0]) {
          temp = this.q[leftChild];
          this.q[leftChild] = this.q[index];
          this.q[index] = temp;
          index = leftChild;
        } else {
          break;
        }
      } else {
        break;
      }
    }
    return first;
  }
}

const [n, m, x, y] = input()
  .split(" ")
  .map((el) => parseInt(el));
const graph = Array.from(Array(n + 1), () => []);

for (let i = 0; i < m; i++) {
  const [u, v, w] = input()
    .split(" ")
    .map((el) => parseInt(el));
  graph[u].push([v, w]);
}

function dij() {
  const h = new PriorityQ();
  h.insert([0, x, 0]);
  const dist = Array.from(Array(n + 1), () => [Infinity, Infinity]);
  const pathCount = Array(n + 1).fill(0);

  dist[x] = [0, 0];
  pathCount[x] = 1;

  while (h.q.length > 0) {
    const [total, now, count] = h.pop();
    if (dist[now][0] >= total && dist[now][1] >= count) {
      for (let [node, weight] of graph[now]) {
        if (total + weight < dist[node][0]) {
          dist[node] = [total + weight, count + 1];
          pathCount[node] = pathCount[now];
          h.insert([total + weight, node, count + 1]);
        } else if (
          total + weight == dist[node][0] &&
          count + 1 < dist[node][1]
        ) {
          dist[node] = [total + weight, count + 1];
          pathCount[node] = pathCount[now];
          h.insert([total + weight, node, count + 1]);
        } else if (
          total + weight == dist[node][0] &&
          count + 1 == dist[node][1]
        ) {
          pathCount[node] += pathCount[now];
          pathCount[node] %= 1000000009;
        }
      }
    }
  }
  return [dist, pathCount];
}

const [d, ptc] = dij();

if (d[y][0] === Infinity) {
  console.log(-1);
} else {
  console.log(d[y][0]);
  console.log(d[y][1]);
  console.log(ptc[y]);
}
