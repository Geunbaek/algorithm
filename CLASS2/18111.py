import sys
input = sys.stdin.readline
from collections import Counter

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m, b = map(int, input().split())
board = []
answer = (10**8, 0)
for _ in range(n):
    line = list(map(int, input().split()))
    board += line

total_block = sum(board)
board = Counter(board)

for i in range(257):
    time = 0
    if (n*m*i) - total_block > b:
        continue
    for key, val in board.items():
        if i < key:
            time += (key - i) * 2 * val
        elif i > key:
            time += (i - key) * val

    if answer[0] > time:
        answer = (time, i)
    elif answer[0] == time and answer[1] < i:
        answer = (time, i)

print(answer[0], answer[1])



