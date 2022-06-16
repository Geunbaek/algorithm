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
  const temp = new Set();

  for (let i = 0; i < n; i++) {
    temp.add(input());
  }

  const ans = [...temp]
    .sort((a, b) => {
      if (a.length === b.length) {
        if (a > b) return 1;
        else if (a < b) return -1;
        else return 0;
      }
      return a.length - b.length;
    })
    .join("\n");

  console.log(ans);
};

solution();
