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

const year = parseInt(input());

if (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)) {
  console.log(1);
} else {
  console.log(0);
}
