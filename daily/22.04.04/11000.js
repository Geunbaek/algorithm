let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString();
let input = fs.readFileSync("ex.txt").toString();

input = input.split("\n").map((el) => el.trim());

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

const n = parseInt(input[0]);
const arr = [];

for (let i = 1; i <= n; i++) {
  const [s, t] = input[i].split(" ").map((el) => parseInt(el));
  arr.push([s, t]);
}

arr.sort((a, b) => a[0] - b[0]);

const pq = new PriorityQ();
pq.insert([arr[0][1], arr[0][0]]);

for (let i = 1; i < arr.length; i++) {
  let [end, start] = pq.pop();
  if (arr[i][0] >= end) {
    pq.insert([arr[i][1], start]);
  } else {
    pq.insert([end, start]);
    pq.insert([arr[i][1], arr[i][0]]);
  }
}

console.log(pq.q.length);
