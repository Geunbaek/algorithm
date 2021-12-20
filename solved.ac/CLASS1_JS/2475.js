let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString();
let input = fs.readFileSync("ex.txt").toString();

input = input.split(" ").map((el) => parseInt(el));

const ans = input.reduce((acc, cur) => {
  return acc + cur * cur;
}, 0);
console.log(ans % 10);
