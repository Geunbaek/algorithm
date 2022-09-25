import re
from collections import deque


def solution(s):
    answer = 1000
    for length in range(1, len(s) + 1):
        splitedS = deque(filter(lambda x: x, re.split(r"([a-z]{" + str(length) + "})", s)))
        stack = []

        while splitedS:
            string = splitedS.popleft()
            if stack and stack[-1][1] == string:
                stack[-1][0] += 1
            else:
                stack.append([1, string])
        result = list(map(lambda x: str(x[0]) + x[1] if x[0] != 1 else x[1], stack))
        answer = min(answer, len("".join(result)))
    return answer