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
  const t = Number(input());
  for (let i = 0; i < t; i++) {
    const n = Number(input());
    const dp = Array.from({ length: n + 1 }, () => [0, 0]);
    dp[0] = [1, 0];
    dp[1] = [0, 1];

    for (let i = 2; i < n + 1; i++) {
      const [z, o] = dp[i - 1];
      dp[i] = [o, o + z];
    }
    console.log(dp[n].join(" "));
  }
};

solution();
