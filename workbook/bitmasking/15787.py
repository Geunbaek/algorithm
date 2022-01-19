import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [deque([0 for _ in range(20)]) for _ in range(n)]
ban = set()

for _ in range(m):
    oper = list(map(int, input().split()))
    if oper[0] == 1:
        graph[oper[1] - 1][oper[2] - 1] = 1
    elif oper[0] == 2:
        graph[oper[1] - 1][oper[2] - 1] = 0
    elif oper[0] == 3:
        graph[oper[1] - 1].pop()
        graph[oper[1] - 1].appendleft(0)
    elif oper[0] == 4:
        graph[oper[1] - 1].popleft()
        graph[oper[1] - 1].append(0)

cnt = 0
for line in graph:
    line = "".join(map(str, line))
    if line not in ban:
        ban.add(line)
        cnt += 1
print(cnt)
