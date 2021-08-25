let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let count = parseInt(input[0].trim());
let numbers = input[1].split(' ').map(el => parseInt(el))
let maxVal = Math.max.apply(null, numbers)

numbers = numbers.map(el => {
  return el / maxVal * 100
})
let total = numbers.reduce((acc, cur)=>{
  return acc += cur
}, 0)

console.log(total / count)