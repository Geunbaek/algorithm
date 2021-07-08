import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
result = deque()

for i in range(len(a)-1, -1, -1):
    if a[i] == 1:
        result.appendleft(n-i)
    elif a[i] == 2:
        result.insert(1, n-i)
    elif a[i] == 3:
        result.append(n-i)


print(*result)

