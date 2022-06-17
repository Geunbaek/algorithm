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
  const stack = [];
  const ans = [];
  for (let i = 0; i < n; i++) {
    const oper = input().split(" ");
    if (oper[0] === "push") {
      stack.push(oper[1]);
    } else if (oper[0] === "pop") {
      ans.push(stack.length === 0 ? -1 : stack.pop());
    } else if (oper[0] === "size") {
      ans.push(stack.length);
    } else if (oper[0] === "empty") {
      ans.push(stack.length === 0 ? 1 : 0);
    } else if (oper[0] === "top") {
      ans.push(stack.length === 0 ? -1 : stack[stack.length - 1]);
    }
  }
  console.log(ans.join("\n"));
};

solution();
