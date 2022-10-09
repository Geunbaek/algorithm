import sys
from collections import deque
input = sys.stdin.readline

def operTonado(x, y, d):
    global answer
    temp = board[y][x]

    # 진행하는 방향 두 칸 뒤 5%
    nx = x + dx[d] * 2
    ny = y + dy[d] * 2

    if 0 <= nx < n and 0 <= ny < n:
        board[ny][nx] += int(board[y][x] * 0.05)
    else:
        answer += int(board[y][x] * 0.05)
    temp -= int(board[y][x] * 0.05)

    # 진행 방향과 수직 오른쪽 한 칸 뒤 7%
    nx = x + dx[d - 2]
    ny = y + dy[d - 2]

    if 0 <= nx < n and 0 <= ny < n:
        board[ny][nx] += int(board[y][x] * 0.07)
    else:
        answer += int(board[y][x] * 0.07)
    temp -= int(board[y][x] * 0.07)

    # 진행 방향과 수직 오른쪽 두 칸 뒤 2%
    nx = x + dx[d - 2] * 2
    ny = y + dy[d - 2] * 2

    if 0 <= nx < n and 0 <= ny < n:
        board[ny][nx] += int(board[y][x] * 0.02)
    else:
        answer += int(board[y][x] * 0.02)
    temp -= int(board[y][x] * 0.02)

    # 진행 방향과 수직 왼쪽 한 칸 뒤 7%
    nx = x + dx[(d + 2) % 8]
    ny = y + dy[(d + 2) % 8]

    if 0 <= nx < n and 0 <= ny < n:
        board[ny][nx] += int(board[y][x] * 0.07)
    else:
        answer += int(board[y][x] * 0.07)
    temp -= int(board[y][x] * 0.07)

    # 진행 방향과 수직 왼쪽 두 칸 뒤 2%
    nx = x + dx[(d + 2) % 8] * 2
    ny = y + dy[(d + 2) % 8] * 2

    if 0 <= nx < n and 0 <= ny < n:
        board[ny][nx] += int(board[y][x] * 0.02)
    else:
        answer += int(board[y][x] * 0.02)
    temp -= int(board[y][x] * 0.02)

    # 진행 방향의 오른쪽 대각선 10%
    nx = x + dx[(d - 1)]
    ny = y + dy[(d - 1)]

    if 0 <= nx < n and 0 <= ny < n:
        board[ny][nx] += int(board[y][x] * 0.1)
    else:
        answer += int(board[y][x] * 0.1)
    temp -= int(board[y][x] * 0.1)

    # 진행 방향의 왼쪽 대각선 10%
    nx = x + dx[(d + 1) % 8]
    ny = y + dy[(d + 1) % 8]

    if 0 <= nx < n and 0 <= ny < n:
        board[ny][nx] += int(board[y][x] * 0.1)
    else:
        answer += int(board[y][x] * 0.1)
    temp -= int(board[y][x] * 0.1)

    # 진행 반대 방향의 오른쪽 대각선 1%
    nx = x + dx[d - 3]
    ny = y + dy[d - 3]

    if 0 <= nx < n and 0 <= ny < n:
        board[ny][nx] += int(board[y][x] * 0.01)
    else:
        answer += int(board[y][x] * 0.01)
    temp -= int(board[y][x] * 0.01)

    # 진행 반대 방향의 왼쪽 대각선 1%
    nx = x + dx[(d + 3) % 8]
    ny = y + dy[(d + 3) % 8]

    if 0 <= nx < n and 0 <= ny < n:
        board[ny][nx] += int(board[y][x] * 0.01)
    else:
        answer += int(board[y][x] * 0.01)
    temp -= int(board[y][x] * 0.01)

    # 진행하는 방향 한 칸 뒤 남은 값
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n:
        board[ny][nx] += temp
    else:
        answer += temp


def moveTonado():
    turn = 0
    q = deque()
    q.append((n // 2, n // 2, 0))
    while q:
        x, y, d = q.popleft()
        movement = turn // 2 + 1
        for i in range(1, movement + 1):
            nx = x + dx[d] * i
            ny = y + dy[d] * i

            operTonado(nx, ny, d)
            board[ny][nx] = 0
            if nx == 0 and ny == 0:
                return
        q.append((nx, ny, (d + 2) % 8))
        turn += 1

n = int(input())
answer = 0
board = []
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(n):
    board.append(list(map(int, input().split())))

moveTonado()
print(answer)