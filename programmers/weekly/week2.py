def solution(scores):
    answer = ''
    for x in range(len(scores)):
        total = 0;
        isMin = True;
        isMax = True;
        for y in range(len(scores)):
            if x != y:
                if scores[x][x] <= scores[y][x]: isMax = False;
                if scores[x][x] >= scores[y][x]: isMin = False;
                total += scores[y][x]
        if isMax or isMin:
            avg = total / (len(scores) - 1)
        else:
            avg = (total + scores[x][x]) / len(scores)
        if avg >= 90: answer += 'A';
        elif avg >= 80: answer += 'B';
        elif avg >= 70: answer += 'C';
        elif avg >= 50: answer += 'D';
        else: answer += 'F'
        
    return answer