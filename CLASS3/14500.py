import sys
input = sys.stdin.readline
from collections import deque

tetromino = [
    [(0,0), (0,1), (1,0), (1,1)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (0,1), (0,2), (1,0)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(1,0), (0,1), (1,1), (2,1)],
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]


def bfs(a, b):
    global ans
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(19):
            val = 0
            for j in tetromino[i]:
                nx = x + j[1]
                ny = y + j[0]
                if 0 <= nx < m and 0 <= ny < n:
                    val += board[ny][nx]
            ans = max(ans, val)

n, m = map(int, input().split())
board = []
ans = 0
for _ in range(n):
    board.append(list(map(int, input().split())))

for y in range(n):
    for x in range(m):
        bfs(x, y)
print(ans)
