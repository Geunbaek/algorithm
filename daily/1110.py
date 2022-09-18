import sys
from collections import deque

input = sys.stdin.readline

N = input().strip()

N = list(N) if len(N) >= 2 else ['0'] + list(N)
q = deque(N)
target = int("".join(N))
count = 0

while True:
    first = q.popleft()
    second = q.popleft()

    _sum = int(first) + int(second)
    newN = second + str(_sum % 10)
    q = deque(list(newN))
    N = list(newN)
    count += 1
    if int("".join(N)) == target:
        print(count)
        break

