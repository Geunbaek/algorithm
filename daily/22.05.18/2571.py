import sys
input = sys.stdin.readline

def paint(x1, y1, x2, y2):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            board[y][x] = 1

n = int(input())
board= [[0 for _ in range(100)] for _ in range(100)]
ans = 0

for _ in range(n):
    left_diff, bottom_diff = map(int, input().split())
    x1, x2 = left_diff, left_diff + 10 - 1
    y1, y2 = 90 - bottom_diff, 100 - bottom_diff - 1
    paint(x1, y1, x2, y2)

for x in range(100):
    for y in range(1, 100):
        if board[y][x] == 0:
            continue
        board[y][x] += board[y - 1][x]


for y in range(100):
    for x in range(100):
        height = 101
        for i in range(x, 100):
            height = min(height, board[y][i])
            if height == 0:
                break
            area = height * (i - x + 1)
            ans = max(ans, area)

print(ans)