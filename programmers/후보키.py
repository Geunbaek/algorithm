from itertools import combinations
from collections import defaultdict


def hasBanIndex(comb, ban):
    for i in range(1, len(comb) + 1):
        for newComb in combinations(comb, i):
            if "-".join(map(str,newComb)) in ban:
                return True
    return False

def solution(relation):
    answer = 0
    col = len(relation[0])
    ban = set()

    for i in range(1, col + 1):
        for comb in combinations([i for i in range(col)], i):
            table = defaultdict(int)

            if hasBanIndex(comb, ban):
                continue

            for r in relation:
                table["".join([r[c] for c in comb])] += 1

            if len(table) == len(relation):
                ban.add("-".join(map(str, comb)))
                answer += 1

    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))