import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    q = deque()
    q.append((0,0,0))
    visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visit[0][0][0] = 1

    while q:
        x, y, bcnt = q.popleft()
        if x == m-1 and y == n-1:
            return visit[y][x][bcnt]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visit[ny][nx][bcnt] == 0:
                    if board[ny][nx] == 0:
                        visit[ny][nx][bcnt] = visit[y][x][bcnt] + 1
                        q.append((nx, ny, bcnt))
                    if bcnt == 0 and board[ny][nx]== 1:
                        visit[ny][nx][1] = visit[y][x][0] + 1
                        q.append((nx, ny, 1))
    return -1

n, m = map(int, input().split())
board = []

for _ in range(n):
    line = list(map(int, input().strip()))
    board.append(line)

ans = bfs()
print(ans)


"""
8 8
01000100
01010100
01010100
01010100
01010100
01010100
01010100
00010100
"""
"""
5 10
0000011000
1101011010
0000000010
1111111110
1111000000
"""


