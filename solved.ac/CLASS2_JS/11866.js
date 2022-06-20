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
  const [n, k] = input().split(" ").map(Number);
  const arr = Array.from({ length: n }, (_, index) => index + 1);
  const ans = [];
  while (arr.length) {
    for (let i = 0; i < k - 1; i++) {
      arr.push(arr.shift());
    }
    ans.push(arr.shift());
  }

  console.log(`<${ans.join(", ")}>`);
};

solution();
