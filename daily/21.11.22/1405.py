import sys
input = sys.stdin.readline

n, E, W, S, N = map(int, input().split())

p = [E/100, W/100, S/100, N/100]

total = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

board = [[0 for _ in range(2 * 15 + 2)] for _ in range(2 * 15 + 2)]

def dfs(x, y, depth, prob):
    global total
    if board[y][x] == 0:
        if depth == n:
            total += prob
            return

        board[y][x] = 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i], depth + 1, prob * p[i])
        board[y][x] = 0

dfs(15, 15, 0, 1)
print(total)
