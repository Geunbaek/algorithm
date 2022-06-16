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

const solution = () => {
  const t = Number(input());
  for (let i = 0; i < t; i++) {
    const [n, m] = input().split(" ").map(Number);
    const pq = input().split(" ").map(Number);
    const q = Array.from({ length: pq.length }, (_, index) => index);

    let max = Math.max(...pq);
    let count = 0;

    while (pq.length) {
      const [p, first] = [pq.shift(), q.shift()];
      if (p === max) {
        max = Math.max(...pq);
        count += 1;
        if (first === m) {
          console.log(count);
          break;
        }
      } else {
        q.push(first);
        pq.push(p);
      }
    }
  }
};

solution();
