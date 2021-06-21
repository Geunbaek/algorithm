import sys
input = sys.stdin.readline
import math
from itertools import combinations

t = int(input())
for _ in range(t):
    n = int(input())
    vector = []
    total_x = 0
    total_y = 0
    ans = 10 ** 9

    for _ in range(n):
        u, v = map(int, input().split())
        total_x += u
        total_y += v
        vector.append((u, v))

    combs = list(combinations(vector, n // 2))
    for comb in combs[:len(combs) // 2]:
        total_x1 = 0
        total_y1 = 0
        for x1, y1 in comb:
            total_x1 += x1
            total_y1 += y1

        total_x2 = total_x - total_x1
        total_y2 = total_y - total_y1

        ans = min(ans, math.sqrt((total_x1 - total_x2) ** 2 + (total_y1 - total_y2) ** 2 ))
    print(ans)


