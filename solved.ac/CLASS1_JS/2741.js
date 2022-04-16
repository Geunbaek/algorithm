const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : fs.readFileSync("ex.txt").toString()
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const n = Number(input());
let answer = "";
for (let i = 1; i <= n; i++) {
  answer += `${i}\n`;
}
console.log(answer);
