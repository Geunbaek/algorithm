def solution(survey, choices):
    MBTIScore = {
        "R": 0, "T": 0,
        "C": 0, "F": 0,
        "J": 0, "M": 0,
        "A": 0, "N": 0,
    }

    for s, c in zip(survey, choices):
        firstMBTI, secondMBTI = list(s)
        if c < 4:
            MBTIScore[firstMBTI] += 4 - c
        elif c > 4:
            MBTIScore[secondMBTI] += c - 4

    result = []
    for MBTI in ("RT", "CF", "JM", "AN"):
        firstMBTI, secondMBTI = list(MBTI)
        firstScore = MBTIScore[firstMBTI]
        secondScore = MBTIScore[secondMBTI]

        if firstScore > secondScore:
            result.append(firstMBTI)
        elif firstScore < secondScore:
            result.append(secondMBTI)
        else:
            result.append(firstMBTI)

    return "".join(result)