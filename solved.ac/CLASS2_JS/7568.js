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
  const info = Array.from({ length: n }, () => input().split(" ").map(Number));

  let prize = Array(n).fill(0);

  for (let y = 0; y < n; y++) {
    let count = 0;
    for (let x = 0; x < n; x++) {
      if (x === y) continue;
      if (info[y][0] < info[x][0] && info[y][1] < info[x][1]) {
        count += 1;
      }
    }
    prize[y] = count + 1;
  }
  console.log(prize.join(" "));
};

solution();
