import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

def isConnectedArea(areas):
    start = None

    for area in areas:
        start = area
        break

    q = deque([start])
    visited = set()
    visited.add(start)

    while q:
        now = q.popleft()
        for _next in graph[now]:
            if _next not in visited and _next in areas:
                visited.add(_next)
                q.append(_next)

    for area in areas:
        if area not in visited:
            return False
    return True

def getTotalCount(areas):
    count = 0
    for area in areas:
        count += electionPrecinct[area - 1]
    return count

n = int(input())
electionPrecinct = list(map(int, input().split()))
arr = [i + 1 for i in range(n)]
visited = [0 for _ in range(n + 1)]
graph = [None]
answer = sys.maxsize

for i in range(n):
    connectionInfo = set(map(int, input().split()[1:]))
    graph.append(connectionInfo)

for i in range(1, n):
    for comb in combinations(arr, i):
        first = set(comb)
        second = set(arr) ^ first
        if isConnectedArea(first) and isConnectedArea(second):
            answer = min(answer, abs(getTotalCount(first) - getTotalCount(second)))

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)