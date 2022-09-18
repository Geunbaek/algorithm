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

const check = (num, ban) => {
  const strNum = num.toString();

  for (let i = 0; i < ban.length; i++) {
    if (strNum.includes(ban[i])) {
      return false;
    }
  }
  return true;
};

const solution = () => {
  const n = input();
  const m = Number(input());
  let ans = Math.abs(Number(n) - 100);
  let arr = [];
  if (m) {
    arr = input().split(" ").map(Number);
  }

  for (let i = 0; i <= 1000000; i++) {
    if (check(i, arr)) {
      ans = Math.min(ans, i.toString().length + Math.abs(Number(n) - i));
    }
  }
  console.log(ans);
};

solution();
