import sys
input = sys.stdin.readline

from collections import deque

def bfs(a, b, area):
    q = deque()
    q.append((a, b))
    visit[b][a] = area
    count = 0

    while q:
        x, y = q.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if board[ny][nx] == 0 and visit[ny][nx] == 0:
                    q.append((nx, ny))
                    visit[ny][nx] = area
    return count

n, m = map(int, input().split())
board = []
visit = [[0 for _ in range(m)] for _ in range(n)]
area = 0
area_size = {}

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for y in range(n):
    line = list(map(int, input().strip()))
    board.append(line)

for y in range(n):
    for x in range(m):
        if board[y][x] == 0 and visit[y][x] == 0:
            area += 1
            area_size[area] = bfs(x, y, area)

for y in range(n):
    for x in range(m):
        if board[y][x] == 1:
            ans = 1
            checked = set()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if visit[ny][nx] != 0 and visit[ny][nx] not in checked:
                        ans += area_size[visit[ny][nx]]
                        checked.add(visit[ny][nx])
            board[y][x] = ans % 10

for b in board:
    print("".join(map(str, b)))

