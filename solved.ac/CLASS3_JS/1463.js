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
  const n = Number(input());
  const dp = Array(1000001).fill(0);

  [dp[1], dp[2], dp[3]] = [0, 1, 1];

  for (let i = 4; i < n + 1; i++) {
    let temp = (dp[i] = dp[i - 1] + 1);
    if (i % 3 === 0) {
      temp = Math.min(temp, dp[i / 3] + 1);
    }
    if (i % 2 === 0) {
      temp = Math.min(temp, dp[i / 2] + 1);
    }
    dp[i] = temp;
  }
  console.log(dp[n]);
};

solution();
