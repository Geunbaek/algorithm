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
  const c = +input();
  const n = +input();
  const graph = Array.from({ length: c + 1 }, () => []);
  const visit = Array(c + 1).fill(0);

  for (let i = 0; i < n; i++) {
    const [u, v] = input().split(" ").map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }

  const bfs = () => {
    const q = [1];
    visit[1] = 1;
    let cnt = 0;

    while (q.length) {
      const now = q.shift();
      cnt += 1;
      for (let i = 0; i < graph[now].length; i++) {
        const next_ = graph[now][i];
        if (visit[next_] === 0) {
          visit[next_] = 1;
          q.push(next_);
        }
      }
    }
    return cnt;
  };
  console.log(bfs() - 1);
};

solution();
