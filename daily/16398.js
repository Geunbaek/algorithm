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

const find = (p, x) => {
  if (p[x] !== x) {
    p[x] = find(p, p[x]);
  }
  return p[x];
};

const union = (p, a, b) => {
  const ap = find(p, a);
  const bp = find(p, b);
  p[ap] = bp;
};

const solution = () => {
  const n = Number(input());
  const map = Array.from({ length: n }, () => input().split(" ").map(Number));
  const p = Array.from({ length: n }, (_, index) => index);
  const edges = [];
  let total = 0;

  for (let y = 0; y < n; y++) {
    for (let x = 0; x < n; x++) {
      if (x !== y) {
        edges.push([x, y, map[y][x]]);
      }
    }
  }

  edges.sort((a, b) => a[2] - b[2]);

  for (const [u, v, c] of edges) {
    if (find(p, u) !== find(p, v)) {
      union(p, u, v);
      total += c;
    }
  }

  console.log(total);
};

solution();
