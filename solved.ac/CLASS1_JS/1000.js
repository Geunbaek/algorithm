const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input = line.split(' ').map((elem) => parseInt(elem));
  console.log(input[0] + input[1]);
  rl.close();
})
