import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def w_split():
    lenw = len(wpos)
    while lenw:
        x, y = wpos.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if board[ny][nx] == '.' or board[ny][nx] == 'S':
                    board[ny][nx] = '*'
                    wpos.append((nx, ny))

        lenw -= 1

def bfs():
    while spos:
        lens = len(spos)
        w_split()
        while lens:
            x, y, cnt = spos.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < c and 0 <= ny < r:
                    if board[ny][nx] == '.':
                        board[ny][nx] = 'S'
                        spos.append((nx, ny, cnt + 1))
                    elif board[ny][nx] == 'D':
                        return cnt + 1
            lens -= 1

r, c = map(int, input().split())
board = []
spos = deque()
wpos = deque()

for y in range(r):
    line = list(map(str, input().strip()))
    for x in range(len(line)):
        if line[x] == 'S':
            spos.append((x, y, 0))
        elif line[x] == '*':
            wpos.append((x, y))

    board.append(line)
ans = bfs()
if ans is None:
    print('KAKTUS')
else:
    print(ans)


