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
  const [n, k] = input().split(" ").map(Number);

  const bfs = (start) => {
    const q = [[start, 0]];
    const visited = Array(100001).fill(100001);
    visited[start] = 0;

    while (q.length) {
      const [now, cnt] = q.shift();
      if (now === k) {
        return cnt;
      }
      for (const next of [now - 1, now + 1, now * 2]) {
        if (0 <= next && next < 100001 && visited[next] > cnt) {
          visited[next] = cnt;
          q.push([next, cnt + 1]);
        }
      }
    }
  };
  console.log(bfs(n));
};

solution();
