const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : fs.readFileSync("ex.txt").toString()
).split("\n");

const input = () => {
  let line = 0;
  return stdin[line++];
};

const n = Number(input());
let ans = "";

for (let i = n; i >= 1; i--) {
  ans += `${i}\n`;
}
console.log(ans);
