import math
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    dist = y - x

    n = int(math.sqrt(dist))
    if dist - n ** 2 == 0:
        print(2 * n - 1)
    elif dist - n ** 2 <= n:
        print(2 * n)
    else:
        print(2 * n + 1)