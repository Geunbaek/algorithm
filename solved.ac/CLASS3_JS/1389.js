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
  const [n, m] = input().split(" ").map(Number);
  const dist = Array.from({ length: n + 1 }, () => Array(n + 1).fill(Infinity));
  let maxCount = Infinity;
  let ans = 0;

  for (let i = 0; i < m; i++) {
    const [a, b] = input().split(" ").map(Number);
    dist[b][a] = 1;
    dist[a][b] = 1;
  }

  for (let z = 1; z < n + 1; z++) {
    for (let y = 1; y < n + 1; y++) {
      for (let x = 1; x < n + 1; x++) {
        dist[y][x] = Math.min(dist[y][x], dist[z][x] + dist[y][z]);
      }
    }
  }
  console.log(dist);

  for (let y = 1; y < n + 1; y++) {
    let sum = 0;
    for (let x = 1; x < n + 1; x++) {
      if (x === y) continue;
      sum += dist[y][x];
    }
    if (maxCount > sum) {
      maxCount = sum;
      ans = y;
    }
  }
  console.log(ans);
};

solution();
