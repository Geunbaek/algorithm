import sys
input = sys.stdin.readline
from collections import deque
# pypy
def operation(s, o):
    if o == "D":
        ret = s * 2 % 10000
    elif o == "S":
        ret = s-1
        if ret < 0:
            ret = 9999
    elif o == 'L':
        ret = s % 1000 * 10 + s//1000
    elif o == 'R':
        ret = s % 10 * 1000 + s//10
    return ret

def bfs(a, b):
    q = deque()
    q.append((a, ""))
    visit = set()
    visit.add(a)
    while q:
        now, ops = q.popleft()
        if now == b:
            return ops
        for i in ("D", "S", "L", "R"):
            new = operation(now, i)
            if new not in visit:
                visit.add(new)
                new_op = ops + i
                q.append((new, new_op))

t = int(input())

for _ in range(t):
    a, b = input().strip().split()
    min_length = 10**10
    result = bfs(int(a), int(b))
    print(result)

"""
1
1234 3412
"""