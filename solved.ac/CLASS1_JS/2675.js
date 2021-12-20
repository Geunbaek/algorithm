let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString();
let input = fs.readFileSync("ex.txt").toString();
input = input.split("\n");
const count = parseInt(input[0]);
for (let i = 1; i < 1 + count; i++) {
  const [n, str] = input[i].split(" ");

  const arr = str.split("").map((el) => el.repeat(parseInt(n)));
  console.log(arr.join(""));
}
