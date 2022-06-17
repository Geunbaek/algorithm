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
  const arr = Array.from({ length: n }, (_, index) => index + 1);
  let firstIdx = 0;

  while (arr.length - firstIdx > 1) {
    const first = arr[firstIdx];
    delete arr[firstIdx];
    firstIdx += 1;
    arr[arr.length] = arr[firstIdx];
    delete arr[firstIdx];
    firstIdx += 1;
  }
  console.log(arr[firstIdx]);
};

solution();
