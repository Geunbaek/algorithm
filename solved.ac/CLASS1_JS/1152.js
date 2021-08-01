const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input = line.split(' ').filter((elem) => elem);
  console.log(input.length);
  rl.close();
})
