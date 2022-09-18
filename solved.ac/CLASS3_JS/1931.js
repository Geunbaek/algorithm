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
  const n = +input();
  const schedules = Array.from({ length: n }, () =>
    input().split(" ").map(Number)
  );
  schedules.sort((a, b) => a[1] - b[1] || a[0] - b[0]);
  let count = 0;
  let time = 0;
  for (let i = 0; i < schedules.length; i++) {
    if (time <= schedules[i][0]) {
      time = schedules[i][1];
      count += 1;
    }
  }
  console.log(count);
};

solution();
