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
  const ans = [];

  for (let i = 0; i < n; i++) {
    const line = input();
    const stack = [];
    let flag = true;

    for (let j = 0; j < line.length; j++) {
      if (line[j] === "(") {
        stack.push(line[j]);
      } else {
        if (!stack.length) {
          flag = false;
          break;
        } else {
          stack.pop();
        }
      }
    }
    if (!flag || stack.length) ans.push("NO");
    else ans.push("YES");
  }
  console.log(ans.join("\n"));
};

solution();
