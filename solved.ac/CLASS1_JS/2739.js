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

const n = input();

Array(9)
  .fill(0)
  .forEach((_, num) => console.log(`${n} * ${num + 1} = ${n * (num + 1)}`));
