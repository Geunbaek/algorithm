def getNDecimal(number, n):
    numberDict = {
        0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
        10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
    }
    nDecimal = ""
    while number >= n:
        nDecimal += str(numberDict[number % n])
        number //= n
    nDecimal += str(numberDict[number])
    return nDecimal[::-1]


def solution(n, t, m, p):
    result = ""
    answers = ""
    num = 0
    while len(answers) < m * t:
        answers += getNDecimal(num, n);
        num += 1

    for turn, answer in enumerate(answers):
        if turn % m == p - 1:
            result += answer

    return result[:t]