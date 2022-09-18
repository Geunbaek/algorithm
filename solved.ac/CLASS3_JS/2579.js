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
  const n = +input();
  const stairs = Array.from({ length: n }, () => +input());
  const dp = Array(301).fill(0);
  dp[0] = stairs[0];
  if (n >= 1) {
    dp[1] = stairs[0] + stairs[1];
  }
  if (n >= 2) {
    dp[2] = Math.max(stairs[2] + stairs[0], stairs[1] + stairs[2]);
  }

  for (let i = 3; i < n; i++) {
    dp[i] = Math.max(
      stairs[i] + dp[i - 2],
      stairs[i] + stairs[i - 1] + dp[i - 3]
    );
  }
  console.log(dp[n - 1]);
};

solution();
