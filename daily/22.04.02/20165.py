import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direct = {"E": 0, "W": 1, "S": 2, "N": 3}

def attack(x, y, d):
    x, y = int(x), int(y)
    d = direct[d]
    q = deque()
    q.append((x - 1, y - 1, board[y - 1][x - 1]))
    cnt = 0

    if state[y -1][x-1] != 1:
        cnt += 1

    while q:
        cur_x, cur_y, val = q.popleft()
        state[cur_y][cur_x] = 1
        for i in range(val - 1):
            nx = cur_x + dx[d] * (i + 1)
            ny = cur_y + dy[d] * (i + 1)
            if 0 <= nx < m and 0 <= ny < n:
                if state[ny][nx] == 1:
                    q.append((nx, ny, 1))
                else:
                    state[ny][nx] = 1
                    q.append((nx, ny, board[ny][nx]))
                    cnt += 1
    return cnt

def guard(x, y):
    x, y = int(x), int(y)
    state[y - 1][x - 1] = 0


n, m, r = map(int, input().split())
state = [[0 for _ in range(m)] for _ in range(n)]
board = []
count = 0

for _ in range(n):
    board.append(list(map(int, input().split())))

for _ in range(r):
    y, x, d = input().strip().split()
    count += attack(x, y, d)
    y1, x1 = input().strip().split()
    guard(x1, y1)

print(count)

for y in range(n):
    for x in range(m):
        print("S" if state[y][x] == 0 else "F", end = " ")
    print()