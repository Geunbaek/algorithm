let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString();
let input = fs.readFileSync('ex.txt').toString();

input = input.split(' ')

let [n, m] = input.map(el => parseInt(el))
let arr = [];
let result = [];

function rec(k){
  if(arr.length === m){
    result.push(arr.join(' '))
    return
  }
  for(let i=k; i <= n; i ++){
    arr.push(i)
    rec(i)
    arr.pop()
  }
}

rec(1)
console.log(result.join('\n'))