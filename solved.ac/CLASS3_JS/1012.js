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

const bfs = (board, a, b, n, m) => {
  const dx = [-1, 0, 1, 0];
  const dy = [0, -1, 0, 1];
  const q = [[a, b]];

  while (q.length) {
    const [x, y] = q.shift();
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
      if (board[ny][nx] === 1) {
        board[ny][nx] = 0;
        q.push([nx, ny]);
      }
    }
  }
};

const solution = () => {
  const t = Number(input());

  for (let i = 0; i < t; i++) {
    const [m, n, k] = input().split(" ").map(Number);
    const board = Array.from({ length: n }, () => Array(m).fill(0));
    let ans = 0;
    for (let j = 0; j < k; j++) {
      const [x, y] = input().split(" ").map(Number);
      board[y][x] = 1;
    }

    for (let y = 0; y < n; y++) {
      for (let x = 0; x < m; x++) {
        if (board[y][x] === 1) {
          bfs(board, x, y, n, m);
          ans += 1;
        }
      }
    }

    console.log(ans);
  }
};

solution();
