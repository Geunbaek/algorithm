import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(b1, b2, b3):
    q = deque()
    ck_board = copy.deepcopy(board)

    for virus in virus_arr:
        q.append((virus[0], virus[1]))

    for b in (b1, b2, b3):
        ck_board[b[1]][b[0]] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if ck_board[ny][nx] == 0:
                    ck_board[ny][nx] = 1
                    q.append((nx, ny))

    cnt = 0
    for y in range(n):
        for x in range(m):
            if ck_board[y][x] == 0:
                cnt += 1
    return cnt




n, m = map(int, input().split())
board = []
zero_arr = []
virus_arr = []

for _ in range(n):
    board.append(list(map(int, input().split())))

for y in range(n):
    for x in range(m):
        if board[y][x] == 0:
            zero_arr.append((x, y))
        if board[y][x] == 2:
            virus_arr.append((x, y))

ck = list(combinations(zero_arr, 3))
result = 0
for elem1, elem2, elem3 in ck:
    result = max(result, bfs(elem1, elem2, elem3))

print(result)



