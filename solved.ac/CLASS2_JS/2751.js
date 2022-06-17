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
  const ans = Array.from({ length: n }, (_, index) => Number(input()))
    .sort((a, b) => a - b)
    .join("\n");
  console.log(ans);
};

solution();
