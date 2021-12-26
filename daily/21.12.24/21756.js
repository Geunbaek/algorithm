let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString();
let input = fs.readFileSync("ex.txt").toString();

input = parseInt(input, 10);

let arr = new Array(input).fill(0).map((el, idx) => idx + 1);

while (arr.length > 1) {
  arr = arr.filter((el, idx) => idx % 2 !== 0);
}
console.log(arr[0]);
