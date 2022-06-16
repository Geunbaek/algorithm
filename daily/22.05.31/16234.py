import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b, c):
    q = deque()
    q.append((a, b))
    path = [(a, b, board[b][a])]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
                if l <= (abs(board[ny][nx] - board[y][x])) <= r:
                    visited[ny][nx] = c
                    q.append((nx, ny))
                    path.append((nx, ny, board[ny][nx]))

    val = sum(map(lambda x: x[-1], path)) // len(path)
    for x, y, c in path:
        board[y][x] = val

    if len(path) > 1:
        return True

    return False


n, l, r = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = 0

for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    count = 1
    check = False
    for y in range(n):
        for x in range(n):
            if visited[y][x] == 0:
                visited[y][x] = count
                if bfs(x, y, count):
                    check = True
                count += 1

    if not check:
        break
    ans += 1


print(ans)