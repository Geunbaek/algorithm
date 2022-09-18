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
  const board = Array.from({ length: n }, () => input().split("").map(Number));

  const bfs = () => {
    const q = [[0, 0, 1]];
    board[0][0] = 0;
    const dx = [-1, 0, 1, 0];
    const dy = [0, -1, 0, 1];

    while (q.length) {
      const [x, y, cnt] = q.shift();
      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];
        if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
        if (nx === m - 1 && ny === n - 1) return cnt + 1;
        if (board[ny][nx] === 1) {
          board[ny][nx] = 0;
          q.push([nx, ny, cnt + 1]);
        }
      }
    }
  };
  console.log(bfs());
};

solution();
