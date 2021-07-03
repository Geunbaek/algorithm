import sys
input = sys.stdin.readline
from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    clothes = defaultdict(int)
    ans = 1
    for _ in range(n):
        name, part = input().strip().split()
        clothes[part] += 1

    for val in clothes.values():
        ans *= (val+1)

    print(ans - 1)


