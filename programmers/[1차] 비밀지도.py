def getBinary(number, n):
    return bin(number)[2:].zfill(n)

def getLine(row1, row2):
    answer = ""
    for c1, c2 in zip(row1, row2):
        if c1 == '1' or c2 == '1':
            answer += '#'
        else:
            answer += ' '
    return answer

def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        answer.append(getLine(getBinary(a, n), getBinary(b, n)))
    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])