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
  const visited = Array(s.length).fill(0);
  const quack = "quack";
  let ans = 0;

  while (true) {
    let index = 0;
    let path = Array(5).fill(-1);
    let flag = true;

    for (let i = 0; i < s.length; i++) {
      if (quack[index] === s[i] && visited[i] === 0) {
        path[index] = i;
        index = index + 1;
      }
      if (index >= 5) {
        path.forEach((p) => {
          visited[p] = 1;
        });
        path = Array(5).fill(-1);
        index = 0;
        flag = false;
      }
    }
    if (flag) break;
    ans += 1;
  }
  console.log(visited.includes(0) ? -1 : ans);
};

solution();
