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
  const [n, m] = input().split(" ").map(Number);
  const arr = input().split(" ").map(Number);

  let [left, right] = [0, Math.max(...arr)];

  while (left <= right) {
    const mid = parseInt((left + right) / 2);
    let temp = 0;

    for (let i = 0; i < arr.length; i++) {
      temp += arr[i] > mid ? arr[i] - mid : 0;
    }

    if (temp >= m) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  console.log(right);
};

solution();
