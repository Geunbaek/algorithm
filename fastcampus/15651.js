let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString();
let input = fs.readFileSync('ex.txt').toString();

input = input.split(' ')

let [n, m] = input.map(el => parseInt(el))
let arr = new Array(m).fill(false)
let result = [];

function rec(k){
  if(k === m){
    result.push(arr.join(' '))
    return
  }
  for(let i=1; i <= n; i ++){
    arr[k] = i
    rec(k+1)
  }
}

rec(0)
console.log(result.join('\n'))


