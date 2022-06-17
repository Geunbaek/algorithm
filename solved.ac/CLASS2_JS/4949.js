const fs = require("fs");
const inputPath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const stdin = fs.readFileSync(inputPath).toString().split("\n");
// .map((line) => line.trim());

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const solution = () => {
  while (true) {
    const line = input();
    if (line === ".") break;

    const stack = [];
    const open = ["(", "["];
    const close = [")", "]"];
    let flag = true;

    for (let char of line) {
      if (open.includes(char)) {
        stack.push(char);
      } else if (close.includes(char)) {
        const index = close.indexOf(char);

        if (stack.length === 0) {
          flag = false;
          break;
        } else if (stack[stack.length - 1] !== open[index]) {
          flag = false;
          break;
        } else {
          stack.pop();
        }
      }
    }
    if (!flag || stack.length) console.log("no");
    else console.log("yes");
  }
};

solution();
