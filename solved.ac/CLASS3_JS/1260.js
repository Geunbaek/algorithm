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

const dfs = (graph, node, visited, ans) => {
  ans.push(node);
  for (let next_ of graph[node]) {
    if (visited[next_] === 0) {
      visited[next_] = 1;
      dfs(graph, next_, visited, ans);
    }
  }
};

const bfs = (graph, start, visited) => {
  const q = [[start]];
  const ans = [];

  while (q.length) {
    const node = q.shift();
    ans.push(node);
    for (let next_ of graph[node]) {
      if (visited[next_] === 0) {
        visited[next_] = 1;
        q.push([next_]);
      }
    }
  }
  return ans.join(" ");
};

const solution = () => {
  const [n, m, v] = input().split(" ").map(Number);
  const graph = Array.from({ length: n + 1 }, () => []);
  const ans = [];

  for (let i = 0; i < m; i++) {
    const [u, v] = input().split(" ").map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }

  for (let i = 0; i < graph.length; i++) {
    graph[i].sort((a, b) => a - b);
  }
  let visited = Array(n + 1).fill(0);
  visited[v] = 1;

  dfs(graph, v, visited, ans);
  console.log(ans.join(" "));

  visited = Array(n + 1).fill(0);
  visited[v] = 1;
  console.log(bfs(graph, v, visited));
};

solution();
