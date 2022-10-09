import sys
from collections import deque
import heapq
input = sys.stdin.readline

def getDist(sx, sy, ex, ey):
    q = deque()
    q.append((sx, sy, 0))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[sy][sx] = 0

    while q:
        x, y, dist = q.popleft()
        if x == ex and y == ey:
            return dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[ny][nx] == 0 and board[ny][nx] != 1:
                    visited[ny][nx] = 1
                    q.append((nx, ny, dist + 1))
    return -1

def find(sx, sy):
    if board[sy][sx] == 2:
        return 0, sy, sx
    ret = []
    q = deque()
    q.append((sx, sy, 0))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    count = peopleCount
    while q:
        x, y, dist = q.popleft()
        if count <= 0:
            return heapq.heappop(ret)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((nx, ny, dist + 1))
                elif board[ny][nx] == 2:
                    visited[ny][nx] = 1
                    q.append((nx, ny, dist + 1))
                    heapq.heappush(ret, ((dist + 1), ny, nx))
                    count -= 1

    if not ret:
        return -1
    return heapq.heappop(ret)

n, m, oil = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

ty, tx = map(lambda x: int(x) - 1, input().split())
people = {}
peopleCount = m

for i in range(m):
    sy, sx, ey, ex = map(int, input().split())
    people[f"{sx-1}-{sy-1}"] = (i, sx - 1, sy - 1, ex - 1, ey - 1)
    board[sy - 1][sx - 1] = 2

while peopleCount > 0:
    p = find(tx, ty)
    if p == -1:
        break

    dist, sy, sx = p
    oil -= dist
    _, _, _, ex, ey = people[f"{sx}-{sy}"]
    dist2 = getDist(sx, sy, ex, ey)

    if dist2 == -1:
        break
    oil -= dist2

    if oil < 0:
        break

    oil += dist2 * 2
    board[sy][sx] = 0
    tx, ty = ex, ey

    peopleCount -= 1

if peopleCount:
    print(-1)
else:
    print(oil)

"""
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
"""