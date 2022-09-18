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
  const s = input();
  const end = Array.from({ length: s.length }, (_, index) =>
    s.slice(index)
  ).sort();
  console.log(end.join("\n"));
};

solution();
