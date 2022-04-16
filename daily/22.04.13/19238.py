import sys
input = sys.stdin.readline
from collections import deque

def bfs(sx, sy, ex, ey):
    q = deque()
    q.append((sx, sy, 0))
    visited = set()

    while q:
        x, y, cnt = q.popleft()
        if x == ex and y == ey:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, cnt + 1))
    return -1

def find(sx, sy, works):
    targets = [(work[0] - 1, work[1] - 1) for work in works]
    q = deque()
    q.append((sx, sy, 0))
    visited = set()
    ret = []

    while q:
        x, y, cnt = q.popleft()
        if ret and ret[-1][-1] < cnt:
            return ret
        if (x, y) in targets:
            ret.append((x, y, cnt))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, cnt + 1))
    if ret:
        return ret
    return -1

n, m, amount = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    board.append(list(map(int, input().split())))

now_y, now_x = map(int, input().split())
works = set()

for i in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    works.add((x1, y1, x2, y2))

while works:
    dists = find(now_x - 1, now_y - 1, works)
    if dists == -1:
        print(-1)
        exit()
    dists.sort(key=lambda x: (x[1], x[0]))
    dist = dists[0]

    target = None
    for work in works:
        if dist[0] + 1 == work[0] and dist[1] + 1 == work[1]:
            target = work

    works.remove(target)
    amount -= dist[-1]

    if amount < 0:
        break

    work_cost = bfs(target[0] - 1, target[1] - 1, target[2] - 1, target[3] - 1)
    if work_cost == -1:
        print(-1)
        exit()
    amount -= work_cost
    if amount < 0:
        break

    amount += work_cost * 2
    now_x, now_y = target[2], target[3]

if amount < 0:
    print(-1)
else:
    print(amount)


"""
5 5 4
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
3 3
2 2 4 2
4 2 4 4
4 4 2 4
2 4 2 2
2 5 3 3
"""


