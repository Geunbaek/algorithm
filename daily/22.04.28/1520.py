import sys
input = sys.stdin.readline
import heapq

def bfs():
    q = []
    heapq.heappush(q, (-board[0][0], 0, 0))
    visit[0][0] = 1

    while q:
        now, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and board[ny][nx] < -now:
                if visit[ny][nx] == 0:
                    heapq.heappush(q, (-board[ny][nx], nx, ny))
                visit[ny][nx] += visit[y][x]


n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
board = []
visit = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, input().split())))

bfs()

print(visit[-1][-1])
