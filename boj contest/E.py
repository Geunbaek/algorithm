import sys
from collections import deque
input = sys.stdin.readline

def fill(count):
    dx = [1, 0]
    dy = [0, 1]
    q = deque()
    q.append((0, 0))
    visit = [[0 for _ in range(n)] for _ in range(n)]
    visit[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[ny][nx] = 0
        board[y][x] = 1
        count -= 1
        if count == 0:
            return
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append((nx, ny))

def fill2(count):
    dx = [-1, 0]
    dy = [0, -1]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((n - 1, n - 1))
    visit[n - 1][n - 1] = 1

    while q:
        x, y = q.popleft()
        if board[y][x] == -1:
            board[y][x] = 2
            count -= 1
            if count <= 0:
                return True
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.append((nx, ny))
    return False

n = int(input())

c, e = map(int, input().split())

board = [[-1 for _ in range(n)] for _ in range(n)]

fill(c)
if fill2(e):
    print(1)
    for b in board:
        print("".join(map(lambda x : str(x) if x != -1 else "0", b)))
else:
    print(-1)



