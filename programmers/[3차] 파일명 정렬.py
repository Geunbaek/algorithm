import re

def solution(files):
    answer = []
    for index, file in enumerate(files):
        head = re.search(r"[a-zA-Z .-]+", file).group().lower()
        number = int(re.search(r"[0-9]+", file).group())
        answer.append((head, number, index, file))

    return list(map(lambda x: x[-1], sorted(answer, key = lambda x: x)))