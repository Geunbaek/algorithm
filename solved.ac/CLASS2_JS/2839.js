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
  let w = 0;

  while (n >= 0) {
    if (n % 5 === 0) {
      w += parseInt(n / 5);
      break;
    } else {
      w += 1;
      n -= 3;
    }
  }
  if (n < 0) {
    console.log(-1);
  } else {
    console.log(w);
  }
};

solution();
