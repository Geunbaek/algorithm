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

const check = (n) => {
  if (n === 1) return false;
  for (let i = 2; i < parseInt(n ** 0.5) + 1; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};

const solution = () => {
  const n = Number(input());
  const ans = input()
    .split(" ")
    .map(Number)
    .reduce((acc, cur) => {
      if (check(cur)) return acc + 1;
      return acc;
    }, 0);
  console.log(ans);
};

solution();
