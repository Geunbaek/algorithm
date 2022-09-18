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
  const map = new Map();
  const ans = [];
  for (let i = 1; i <= n; i++) {
    const name = input();
    map[name] = i;
    map[i] = name;
  }

  for (let i = 1; i <= m; i++) {
    const search = input();
    ans.push(map[search]);
  }
  console.log(ans.join("\n"));
};

solution();
