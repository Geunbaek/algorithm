import sys
input = sys.stdin.readline
from collections import deque

def open():
    for y in range(h + 2):
        for x in range(w + 2):
            if board[y][x].lower() in keys:
                board[y][x] = '.'

def bfs():
    q = deque()
    q.append((0, 0))
    count = 0
    visit = [[0 for _ in range(w + 2)] for _ in range(h + 2)]
    visit[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w + 2 and 0 <= ny < h + 2 and visit[ny][nx] == 0:
                if board[ny][nx] in lower_alpha:
                    visit[ny][nx] = 1
                    keys.add(board[ny][nx])
                    q.append((nx, ny))
                    board[ny][nx] = '.'
                elif board[ny][nx] == '.':
                    visit[ny][nx] = 1
                    q.append((nx, ny))
                elif board[ny][nx] == "$":
                    count += 1
                    visit[ny][nx] = 1
                    q.append((nx, ny))
                    board[ny][nx] = '.'

    return count


t = int(input())
lower_alpha = {chr(i) for i in range(ord('a'), ord("a") + 26)}
upper_alpha = {chr(i) for i in range(ord('A'), ord("A") + 26)}

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(t):
    h, w = map(int, input().split())
    board = [['.' for _ in range(w + 2)]]
    q = deque()
    count = 0

    for y in range(h):
        line = ["."] + list(input().strip()) + ["."]
        board.append(line)
    board.append(['.' for _ in range(w + 2)])

    keys = set(list(input().strip()))
    if '0' in keys:
        keys = set()

    while True:
        if keys:
            open()
            keys = set()
        count += bfs()
        if not keys:
            break

    print(count)







