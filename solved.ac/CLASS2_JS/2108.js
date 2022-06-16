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
  const arr = Array.from({ length: n }, () => Number(input())).sort(
    (a, b) => a - b
  );

  const sum = arr.reduce((acc, cur) => acc + cur, 0);
  const max = new Map();

  for (let num of arr) {
    const count = max.get(num) || 0;
    max.set(num, count + 1);
  }

  let maxArr = [];
  let count = 0;

  for (const [key, val] of max) {
    if (val > count) {
      count = val;
      maxArr = [key];
    } else if (count === val) {
      maxArr.push(key);
    }
  }

  maxArr.sort((a, b) => a - b);
  console.log(Math.round(sum / n).toString());
  console.log(arr[(arr.length - 1) / 2]);
  console.log(maxArr.length === 1 ? maxArr[0] : maxArr[1]);
  console.log(arr[arr.length - 1] - arr[0]);
};

solution();
