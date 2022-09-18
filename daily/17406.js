const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const stdin = fs
  .readFileSync(inputPath)
  .toString()
  .split("\n")
  .map((line) => line.trim())
  .filter((line) => line);

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const perm = (depth, k, visited, path, p) => {
  if (depth >= k - 1) {
    p.push(path);
  }
  for (let i = 0; i < k; i++) {
    if (visited[i] === 0) {
      visited[i] = 1;
      perm(depth + 1, k, visited, path.concat(i), p);
      visited[i] = 0;
    }
  }
};

const oper = (graph, r, c, s) => {
  const dx = [1, 0, -1, 0];
  const dy = [0, 1, 0, -1];
  const q = [[r - s, c - s, graph[r - s][c - s], 0]];

  while (q.length) {
    let [y, x, val, d] = q.shift();

    let nx = x + dx[d];
    let ny = y + dy[d];
    if (ny < r - s || ny > r + s || nx < c - s || nx > c + s) {
      d += 1;
      if (d >= 4) break;
      nx = x + dx[d];
      ny = y + dy[d];
    }
    q.push([ny, nx, graph[ny][nx], d]);
    graph[ny][nx] = val;
  }
};

const getMinRow = (graph) => {
  let temp = Infinity;
  for (let y = 0; y < graph.length; y++) {
    let sum = 0;
    for (let x = 0; x < graph[y].length; x++) {
      sum += graph[y][x];
    }
    temp = Math.min(temp, sum);
  }
  return temp;
};

const solution = () => {
  const [n, m, k] = input().split(" ").map(Number);
  const board = Array.from({ length: n }, () => input().split(" ").map(Number));
  const visited = Array(k).fill(0);

  const opers = [];
  const ans = [];
  const p = [];

  for (let i = 0; i < k; i++) {
    const [r, c, s] = input().split(" ").map(Number);
    opers.push([r, c, s]);
  }

  for (let i = 0; i < k; i++) {
    visited[i] = 1;
    perm(0, k, visited, [i], p);
    visited[i] = 0;
  }

  for (const path of p) {
    const copyGraph = Array.from({ length: board.length }, (_, i) => [
      ...board[i],
    ]);

    for (const index of path) {
      const [r, c, s] = opers[index];
      for (let i = 1; i <= s; i++) {
        oper(copyGraph, r - 1, c - 1, i);
      }
    }
    ans.push(getMinRow(copyGraph));
  }

  console.log(Math.min(...ans));
};

solution();
