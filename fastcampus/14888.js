let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n').map(el => el.trim());
let input = fs.readFileSync('ex.txt').toString().split('\n').map(el => el.trim());

const n = parseInt(input[0])
const arr = input[1].split(' ').map(el => parseInt(el))
const oper = input[2].split(' ')
const result = []

function rec(n, depth, result){
  if(depth === arr.length){
    result.push(n)
    return
  }
  for(let i = 0; i < oper.length; i ++){
    if(oper[i] > 0){
      oper[i] -= 1
      let newN;
      if(i === 0){
        newN = n + arr[depth]
      } else if (i === 1){
        newN = n - arr[depth]
      } else if (i === 2){
        newN = n * arr[depth]
      } else{
        if(n < 0){
          newN = parseInt(-n / arr[depth])
          newN = -newN
        } else {
          newN = parseInt(n / arr[depth])
        }
      }
      if(newN === -0){
        newN = 0
      }
      rec(newN, depth + 1, result)
      oper[i] += 1
    }
  }
}

rec(arr[0], 1, result)
result.sort((a, b)=> a-b)
console.log(result[result.length-1])
console.log(result[0])