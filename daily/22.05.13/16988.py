import sys
input = sys.stdin.readline
from collections import deque

def oper():
    visit = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] == 2 and visit[y][x] == 0:
                result = bfs(x, y, visit)
                if result:
                    count += result

    return count if count else 0


def bfs(a, b, visit):
    q = deque()
    q.append((a, b))
    visit[b][a] = 1
    count = 0
    flag = False

    while q:
        x, y = q.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if board[ny][nx] == 2 and visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append((nx, ny))
                elif board[ny][nx] == 0:
                    flag = True
    if flag:
        return None
    return count



n, m = map(int, input().split())
board = []
empty = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = 0

for y in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for x in range(m):
        if line[x] == 0:
            empty.append((x, y))

for i in range(len(empty)):
    for j in range(i + 1, len(empty)):
        x1, y1 = empty[i]
        x2, y2 = empty[j]
        board[y1][x1] = 1
        board[y2][x2] = 1
        ans = max(ans, oper())
        board[y1][x1] = 0
        board[y2][x2] = 0

print(ans)

