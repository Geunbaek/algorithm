let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString();

input = parseInt(input)

for(let i=1; i<=input; i++){
  for(let k=0; k < input-i; k++){
    process.stdout.write(' ');
  }
  for(let j=0;j<i; j ++){
    process.stdout.write('*');
  }
  console.log()
}


