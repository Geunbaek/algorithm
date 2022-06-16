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
  const a = new Set(input().split(" ").map(Number));
  const m = Number(input());
  const ans = input()
    .split(" ")
    .map((el) => {
      if (a.has(Number(el))) return 1;
      return 0;
    })
    .join("\n");
  console.log(ans);
};

solution();
