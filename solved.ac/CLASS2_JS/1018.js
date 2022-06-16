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

const check = (board, a, b, even, odd) => {
  let count = 0;
  for (let y = 0; y < 8; y++) {
    for (let x = 0; x < 8; x++) {
      if ((x + y) % 2 === 0 && board[b + y][a + x] !== even) {
        count += 1;
      } else if ((x + y) % 2 !== 0 && board[b + y][a + x] !== odd) {
        count += 1;
      }
    }
  }

  return count;
};

const solution = () => {
  const [n, m] = input().split(" ");
  const board = [];
  let ans = Infinity;

  for (let i = 0; i < n; i++) {
    const line = input();
    board.push(line);
  }

  for (let y = 0; y <= n - 8; y++) {
    for (let x = 0; x <= m - 8; x++) {
      ans = Math.min(ans, check(board, x, y, "W", "B"));
      ans = Math.min(ans, check(board, x, y, "B", "W"));
    }
  }
  console.log(ans);
};

solution();
