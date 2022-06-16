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
  const [m, n] = input().split(" ").map(Number);
  const arr = Array(n + 1).fill(0);
  const ans = [];

  for (let i = 2; i < n + 1; i++) {
    if (arr[i] === 0) {
      if (i >= m) {
        ans.push(i);
      }
      for (let j = i + i; j <= n; j += i) {
        arr[j] = 1;
      }
    }
  }
  console.log(ans.join("\n"));
};

solution();
