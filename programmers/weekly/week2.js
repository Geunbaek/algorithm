function solution(scores) {
    var answer = '';
    for(let x = 0; x < scores.length; x ++){
        let isMax = true;
        let isMin = true;
        let avg;
        let total = 0;
        for(let y = 0; y < scores.length; y++){
            if(y !== x){
               if(scores[x][x] <= scores[y][x]) isMax = false;
               if(scores[x][x] >= scores[y][x]) isMin = false;
               total += scores[y][x]
           }
        }
        if(isMax || isMin) avg = total / (scores.length-1);
        else {
            total += scores[x][x];
            avg = total / scores.length
        }
        if(avg >= 90) answer += 'A';
        else if(avg >= 80) answer += 'B';
        else if(avg >= 70) answer += 'C';
        else if(avg >= 50) answer += 'D';
        else answer += "F";
    }
    return answer;
}