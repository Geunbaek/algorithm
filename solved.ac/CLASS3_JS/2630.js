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
  const n = +input();
  const board = Array.from({ length: n }, () => input().split(" ").map(Number));
  const ans = [0, 0];

  const check = (x1, y1, x2, y2, target) => {
    for (let y = y1; y < y2; y++) {
      for (let x = x1; x < x2; x++) {
        if (board[y][x] !== target) return false;
      }
    }
    return true;
  };

  const recur = (x1, y1, x2, y2, len) => {
    const target = board[y1][x1];
    if (check(x1, y1, x2, y2, target)) {
      ans[target] += 1;
      return;
    }

    const nextLen = (len / 2) | 0;
    for (let y = y1; y < y2; y += nextLen) {
      for (let x = x1; x < x2; x += nextLen) {
        recur(x, y, x + nextLen, y + nextLen, nextLen);
      }
    }
  };
  recur(0, 0, n, n, n);
  console.log(ans.join("\n"));
};

solution();
