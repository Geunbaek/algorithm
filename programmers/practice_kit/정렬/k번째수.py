def solution(array, commands):
    answer = []
    for s, e, i in commands:
        temp = sorted(array[s-1 : e])
        answer.append(temp[i-1])
    return answer