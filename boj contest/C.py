import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def bfs(a, b):
    q = deque()
    for i in range(8):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if board[ny][nx] in mbti[2]:
                q.append((nx, ny, 2, i))

    count = 0
    while q:
        x, y, cnt, d = q.popleft()
        if cnt >= 4:
            count += 1
            continue

        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < m and 0 <= ny < n:
            if board[ny][nx] in mbti[cnt + 1]:
                q.append((nx, ny, cnt + 1, d))

    return count

n, m = map(int, input().split())
board = []
mbti = {1: ["E", "I"], 2: ["N", "S"], 3: ["F", "T"], 4: ["P", "J"]}

for _ in range(n):
    board.append(input().strip())

ans = 0
for y in range(n):
    for x in range(m):
        if board[y][x] in mbti[1]:
            ans += bfs(x, y)

print(ans)