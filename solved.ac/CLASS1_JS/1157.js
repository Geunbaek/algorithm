const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let result = {};

rl.on('line', (line) => {
    input = line.split(/([a-zA-Z])/).filter((elem) => elem)
    input.forEach((elem) => {
        elem = elem.toUpperCase();
        if(!result.hasOwnProperty(elem)){ 
            result[elem] = 1;
        } else {
            result[elem] += 1;
        }
  })
    let maxVal = Math.max.apply(null, Object.values(result));
    let ans = [];

    for(key of Object.keys(result)){
        if(result[key] === maxVal){
            ans.push(key);
        }
    }
    if(ans.length === 1){
        console.log(ans[0]);
    }else{
        console.log('?')
    }
    rl.close();
})




