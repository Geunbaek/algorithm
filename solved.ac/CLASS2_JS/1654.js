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
  const [k, n] = input().split(" ").map(Number);
  const arr = Array.from({ length: k }, () => Number(input()));
  const MAX_LEN = Math.max(...arr);

  let [left, right] = [0, MAX_LEN];

  while (left <= right) {
    const mid = parseInt((left + right) / 2);
    let count = 0;
    for (let i = 0; i < k; i++) {
      count += parseInt(arr[i] / mid);
    }

    if (count < n) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  console.log(right);
};

solution();
