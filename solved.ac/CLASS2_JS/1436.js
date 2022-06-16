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
  let count = 0;

  for (let i = 0; i < 10000000; i++) {
    if (i.toString().includes("666")) {
      count += 1;
    }
    if (count === n) {
      console.log(i);
      break;
    }
  }
};

solution();
