import sys
input = sys.stdin.readline
import heapq

def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if board[ny][nx] == "g":
                return 1
    return 0

def bfs():
    q = []
    visit[start[1]][start[0]] = 1
    heapq.heappush(q, (0, 0, start[0], start[1]))
    ret = []
    while q:
        gar, next_gar, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if board[ny][nx] == "." and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    heapq.heappush(q, (gar, next_gar + check(nx, ny), nx, ny))
                elif board[ny][nx] == 'g' and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    heapq.heappush(q, (gar + 1, next_gar, nx, ny))
                elif board[ny][nx] == 'F':
                    ret.append((gar, next_gar))
    return ret


n, m = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visit = [[0 for _ in range(m)] for _ in range(n)]

for y in range(n):
    line = list(input().strip())
    board.append(line)
    for x in range(m):
        if line[x] == 'S':
            start = (x, y)

ans = bfs()
ans.sort()
print(*ans[0])

