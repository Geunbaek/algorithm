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
  const n = Number(input());
  const arr = Array.from({ length: n }, () => input()).sort((a, b) => {
    const [age, name] = a.split(" ");
    const [age2, name2] = b.split(" ");
    return Number(age) - Number(age2);
  });
  console.log(arr.join("\n"));
};

solution();
