import re
from collections import defaultdict


def solution(s):
    answer = defaultdict(int)
    results = re.split(r"{([0-9|,]+)}", s)[1:-1]
    for result in results:
        numbers = list(map(lambda x: int(x), filter(lambda x: x, result.split(","))))
        for num in numbers:
            answer[num] += 1

    return list(map(lambda x: x[0], sorted(answer.items(), key=lambda x: (-x[1], x[0]))))