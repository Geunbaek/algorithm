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
  let n = Number(input());
  let ans = 0;
  while (n > 0) {
    n = parseInt(n / 5, 10);
    ans += n;
  }

  console.log(ans);
};

solution();
