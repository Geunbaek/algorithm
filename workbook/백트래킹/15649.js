let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString();
// let input = fs.readFileSync("ex.txt").toString();

const [n, m] = input.split(" ");
const visit = new Array(parseInt(n) + 1).fill(0);

function recur(cnt, path) {
  if (cnt >= m) {
    console.log(path.join(" "));
    return;
  }
  for (let i = 1; i < n + 1; i++) {
    if (visit[i] === 0) {
      visit[i] = 1;
      recur(cnt + 1, path.concat(i));
      visit[i] = 0;
    }
  }
}
recur(0, []);
