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
  const [n, m] = input().split(" ").map(Number);

  const g = Array.from({ length: n }, () => {
    const [name, songs] = input().split(" ");
    let bin = 0;
    for (let i = 0; i < m; i++) {
      if (songs[i] === "Y") bin |= 1 << i;
    }
    return [name, bin];
  });
  let maxSong = 0;
  let ans = -1;
  const countG = (num) => {
    let cnt = 0;
    while (num) {
      cnt += num & 1;
      num >>= 1;
    }
    return cnt;
  };

  const recur = (cnt, state, index) => {
    const nowSongCount = countG(state);

    if (nowSongCount > maxSong) {
      maxSong = nowSongCount;
      ans = cnt;
    } else if (nowSongCount === maxSong) {
      if (ans > cnt) {
        ans = cnt;
      }
    }

    if (index === n) return;

    recur(cnt + 1, state | g[index][1], index + 1);
    recur(cnt, state, index + 1);
  };

  recur(0, 0, 0);
  console.log(ans);
};

solution();
