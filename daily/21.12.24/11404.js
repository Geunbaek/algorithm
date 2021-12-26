let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString();
//let input = fs.readFileSync("ex.txt").toString();

input = input.split("\n").map((el) => el.trim());
let n = parseInt(input[0]);
let INF = Number.MAX_SAFE_INTEGER;
let graph = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(INF));

for (let y = 0; y < n + 1; y++) {
  for (let x = 0; x < n + 1; x++) {
    if (x === y) {
      graph[y][x] = 0;
    }
  }
}

for (let i = 2; i < input.length; i++) {
  let [a, b, c] = input[i].split(" ").map(Number);
  graph[a][b] = Math.min(graph[a][b], c);
}

for (let z = 0; z < n + 1; z++) {
  for (let y = 0; y < n + 1; y++) {
    for (let x = 0; x < n + 1; x++) {
      graph[y][x] = Math.min(graph[y][x], graph[y][z] + graph[z][x]);
    }
  }
}

for (let y = 0; y < n + 1; y++) {
  for (let x = 0; x < n + 1; x++) {
    if (graph[y][x] === INF) {
      graph[y][x] = 0;
    }
  }
}

graph.splice(1).forEach((el) => {
  console.log(el.splice(1).join(" "));
});
