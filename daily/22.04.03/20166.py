import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b, s):
    q = deque()
    q.append((a, b, 1))
    count = 0

    while q:
        x, y, index = q.popleft()
        if index == len(s):
            count += 1
            continue

        for i in range(8):
            nx = (x + dx[i]) % m
            ny = (y + dy[i]) % n
            if board[ny][nx] == s[index]:
                q.append((nx, ny, index + 1))

    return count

n, m, k = map(int, input().split())
board = []
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
alpha = {}

for _ in range(n):
    board.append(list(input().strip()))

for _ in range(k):
    string = input().strip()
    if string in alpha:
        print(alpha[string])
        continue
    ans = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] == string[0]:
                ans += bfs(x, y, string)
    alpha[string] = ans
    print(ans)