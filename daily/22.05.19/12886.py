import sys
input = sys.stdin.readline
from collections import deque

a, b, c = map(int, input().split())
q = deque()
q.append((a, b, c))
visit = set()

while q:
    x, y, z = q.popleft()
    if x == y == z:
        print(1)
        break

    for i, j, k in [(x, y, z), (x, z, y), (y, z, x)]:
        if (i, j, k) in visit:
            continue

        visit.add((i, j, k))
        if i > j:
            i -= j
            j += j
        else:
            j -= i
            i += i
        q.append((i, j, k))

else:
    print(0)
