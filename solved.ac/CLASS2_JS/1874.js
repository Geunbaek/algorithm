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
  const arr = Array.from({ length: n }, () => Number(input()));
  const ans = [];
  const temp = [];

  for (let i = 1; i <= n; i++) {
    temp.push(i);
    ans.push("+");
    while (temp.length && temp[temp.length - 1] === arr[0]) {
      temp.pop();
      arr.shift();
      ans.push("-");
    }
  }
  if (temp.length) {
    console.log("NO");
  } else {
    console.log(ans.join("\n"));
  }
};

solution();
