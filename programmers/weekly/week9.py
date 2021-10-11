from collections import Counter


def find_p(p, x):
    if p[x] != x:
        p[x] = find_p(p, p[x])
    return p[x]


def union(p, a, b):
    ap = find_p(p, a)
    bp = find_p(p, b)
    p[bp] = ap


def solution(n, wires):
    answer = 10000000
    for i in range(len(wires)):
        p = [i for i in range(n + 1)]
        for idx, wire in enumerate(wires):
            if i != idx:
                if find_p(p, wire[0]) != find_p(p, wire[1]):
                    union(p, wire[0], wire[1])
        for i in range(1, n + 1):
            find_p(p, i)
        cnt = Counter(p).most_common(2)
        answer = min(answer, abs(cnt[0][1] - cnt[1][1]))

    return answer