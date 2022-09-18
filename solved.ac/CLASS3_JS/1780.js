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
  const paper = Array.from({ length: n }, () => input().split(" ").map(Number));
  const ans = [0, 0, 0];

  const oper = (x1, y1, x2, y2, l) => {
    let flag = false;
    const target = paper[y1][x1];
    for (let y = y1; y < y2; y++) {
      for (let x = x1; x < x2; x++) {
        if (paper[y][x] !== target) {
          flag = true;
          break;
        }
      }
      if (flag) break;
    }

    if (flag) {
      const nextL = (l / 3) | 0;
      for (let y = y1; y < y2; y += nextL) {
        for (let x = x1; x < x2; x += nextL) {
          oper(x, y, x + nextL, y + nextL, nextL);
        }
      }
    } else {
      ans[target + 1] += 1;
    }
  };
  oper(0, 0, n, n, n);
  console.log(ans.join("\n"));
};

solution();
