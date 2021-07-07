import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
q = deque([i + 1 for i in range(n)])

numbers = deque(list(map(int, input().split())))
cnt = 0

while numbers:
    target = numbers[0]
    index = q.index(target)
    if index > len(q) // 2:
        while q and q[0] != target:
            q.appendleft(q.pop())
            cnt += 1

    else:
        while q and q[0] != target:
            q.append(q.popleft())
            cnt += 1

    q.popleft()
    numbers.popleft()

print(cnt)

