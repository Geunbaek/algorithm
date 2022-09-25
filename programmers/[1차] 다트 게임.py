import re


def solution(dartResult):
    answer = []
    bonuses = {"S": 1, "D": 2, "T": 3}

    for scoreInfo in list(filter(lambda x: x, re.split(r"([0-9]+[SDT][*#]?)", dartResult))):
        score = ""
        otherScore = ""
        for char in scoreInfo:
            if char.isdigit():
                score += char
            else:
                otherScore += char

        bonus = otherScore[0]
        nowScore = int(score) ** bonuses[bonus]
        if len(otherScore) == 2:
            option = otherScore[1]
            if option == '*':
                if answer:
                    answer[-1] *= 2
                answer.append(int(score) ** bonuses[bonus] * 2)
            else:
                answer.append(int(score) ** bonuses[bonus] * -1)
        else:
            answer.append(int(score) ** bonuses[bonus])

    return sum(answer)