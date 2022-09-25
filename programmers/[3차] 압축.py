from collections import deque


def solution(msg):
    alpha = {chr(i + ord('A')): i + 1 for i in range(26)}
    answer = []
    maxAlphaIndex = 27
    msg = deque(msg)
    while msg:
        nowString = msg.popleft()

        while msg and nowString + msg[0] in alpha:
            nowString += msg.popleft()

        answer.append(alpha[nowString])
        if msg:
            alpha[nowString + msg[0]] = maxAlphaIndex
        maxAlphaIndex += 1

    return answer