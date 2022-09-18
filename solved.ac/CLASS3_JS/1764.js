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
  const noHear = new Set();
  const noSee = new Set();

  for (let i = 0; i < n; i++) {
    const name = input();
    noHear.add(name);
  }

  for (let i = 0; i < m; i++) {
    const name = input();
    noSee.add(name);
  }
  const ans = [...noHear].filter((name) => noSee.has(name)).sort();

  console.log(ans.length);
  console.log(ans.join("\n"));
};
solution();
