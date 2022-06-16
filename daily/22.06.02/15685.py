import sys
input = sys.stdin.readline
from collections import deque

def oper(a, b, d, g):
    temp = [d]
    nx = a + dx[d]
    ny = b + dy[d]

    board[b][a] = 1
    board[ny][nx] = 1

    while g:
        q = deque(temp[::-1])
        while q:
            d = q.popleft()
            nx = nx + dx[(d + 1) % 4]
            ny = ny + dy[(d + 1) % 4]
            board[ny][nx] = 1
            temp.append(d + 1)
        g -= 1

n = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
ans = 0

for _ in range(n):
    x, y, d, g = list(map(int, input().split()))
    oper(x, y, d, g)

for y in range(100):
    for x in range(100):
        if board[y][x] and board[y + 1][x] and board[y][x + 1] and board[y + 1][x + 1] == 1:
            ans += 1

print(ans)



