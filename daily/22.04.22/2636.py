import sys
input = sys.stdin.readline
from collections import deque

def edge_check(a, b):
    q = deque()
    q.append((a, b))
    visit[b][a] = 2
    edges = set()
    flag = False

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visit[ny][nx] == 0 and board[ny][nx] == 0:
                    visit[ny][nx] = 2
                    q.append((nx, ny))
                elif visit[ny][nx] == 0 and board[ny][nx] == 1:
                    edges.add((nx, ny))
            else:
                flag = True
    if flag:
        return edges
    return set()


n, m = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
time = 0
count = 0

for y in range(n):
    line = list(map(int, input().split()))
    board.append(line)

while True:
    visit = [[0 for _ in range(m)] for _ in range(n)]
    edges = []
    for y in range(n):
        for x in range(m):
            if board[y][x] == 0 and visit[y][x] == 0:
                edges += list(edge_check(x, y))

    if not edges:
        break

    count = len(edges)

    for x, y in edges:
        board[y][x] = 0

    time += 1

print(time)
print(count)





