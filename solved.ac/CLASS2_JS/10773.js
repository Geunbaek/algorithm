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
  const k = Number(input());
  const stack = [];
  for (let i = 0; i < k; i++) {
    const num = Number(input());
    if (num === 0) {
      stack.pop();
    } else {
      stack.push(num);
    }
  }
  console.log(stack.reduce((acc, cur) => acc + cur, 0));
};

solution();
