let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString();
let input = fs.readFileSync("ex.txt").toString();

input = input.split("\n").map((el) => parseInt(el));
let ans = [-1, -1];
input.forEach((el, idx) => {
  if (el > ans[0]) {
    ans = [el, idx + 1];
  }
});

console.log(ans[0], ans[1]);
