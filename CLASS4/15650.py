import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())
arr = list(permutations([i for i in range(1, n+1)], m))

for l in arr:
    if sorted(l) == list(l):
        for i in l:
            print(i, end = ' ')
        print()


