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

let [h, m] = input()
  .split(" ")
  .map((el) => parseInt(el));

const alarm = h * 60 + m - 45;

const getHourMin = (time) => {
  let [x, y] = [parseInt(time / 60), time % 60];
  return [x, y];
};

if (alarm < 0) {
  [h, m] = getHourMin(1440 + alarm);
} else {
  [h, m] = getHourMin(alarm);
}

console.log(h, m);
