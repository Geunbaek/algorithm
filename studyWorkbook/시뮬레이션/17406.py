import sys, copy
from collections import deque
from itertools import permutations

input = sys.stdin.readline


def rotate(board, r, c, s):
    q = deque()
    result = board[r][c]

    for i in range(1, s + 1):
        q.append((r - i, c - i, 2 * i, 2 * i, 0, board[r - i][c - i]))

    while q:
        y, x, totalCount, count, d, prev = q.popleft()
        result += prev

        if count <= 0:
            count = totalCount
            d += 1

        if d >= 4:
            continue
        nx = x + dx[d]
        ny = y + dy[d]

        q.append((ny, nx, totalCount, count - 1, d, board[ny][nx]))
        board[ny][nx] = prev
    return result


n, m, k = map(int, input().split())
board = []
operators = []
answer = sys.maxsize

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    board.append(list(map(int, input().split())))

for _ in range(k):
    r, c, s = map(int, input().split())
    operators.append((r - 1, c - 1, s))

for perm in permutations(operators, len(operators)):
    newBoard = copy.deepcopy(board)
    for oper in perm:
        r, c, s = oper
        rotate(newBoard, r, c, s)

    for line in newBoard:
        answer = min(answer, sum(line))

print(answer)