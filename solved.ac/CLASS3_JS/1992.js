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
  const n = Number(input());
  const board = Array.from({ length: n }, () => input().split("").map(Number));

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
    if (len === 2) {
      if (check(x1, y1, x2, y2, target)) return target;
      return `(${[
        ...board[y1].slice(x1, x2),
        ...board[y1 + 1].slice(x1, x2),
      ].join("")})`;
    }

    if (check(x1, y1, x2, y2, target)) return target;

    const nextLen = (len / 2) | 0;
    const temp = [];
    for (let y = y1; y < y2; y += nextLen) {
      for (let x = x1; x < x2; x += nextLen) {
        temp.push(recur(x, y, x + nextLen, y + nextLen, nextLen));
      }
    }
    return `(${temp.join("")})`;
  };
  console.log(recur(0, 0, n, n, n));
};

solution();
