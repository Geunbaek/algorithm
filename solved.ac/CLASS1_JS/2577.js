let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString();
let input = fs.readFileSync("ex.txt").toString();

input = input.split("\n").map((el) => parseInt(el));
const num = (input[0] * input[1] * input[2]).toString();
const arr = new Array(10).fill(0);
for (let n of num) {
  arr[parseInt(n)] += 1;
}
for (let i of arr) {
  console.log(i);
}
