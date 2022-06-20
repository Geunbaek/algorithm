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
  const [n, m, b] = input().split(" ").map(Number);
  const board = Array.from({ length: n }, () => input().split(" ").map(Number));
  let ansTime = Infinity;
  let ansHeight = 0;

  for (let z = 0; z <= 256; z++) {
    let total = b;
    let time = 0;
    for (let y = 0; y < n; y++) {
      for (let x = 0; x < m; x++) {
        if (board[y][x] >= z) {
          const temp = board[y][x] - z;
          total += temp;
          time += temp * 2;
        } else {
          const temp = z - board[y][x];
          total -= temp;
          time += temp * 1;
        }
      }
    }
    if (total >= 0 && ansTime >= time) {
      ansTime = time;
      ansHeight = z;
    }
  }
  console.log(ansTime, ansHeight);
};

solution();
