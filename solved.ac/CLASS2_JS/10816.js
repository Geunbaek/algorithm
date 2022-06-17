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
  const arr = input().split(" ").map(Number);

  const map = new Map();

  for (const el of arr) {
    const count = map.get(el) || 0;
    map.set(el, count + 1);
  }

  const m = Number(input());
  const arr2 = input().split(" ").map(Number);
  const ans = [];

  for (const el of arr2) {
    ans.push(map.get(el) || 0);
  }
  console.log(ans.join(" "));
};

solution();
