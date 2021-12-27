import sys, copy
input = sys.stdin.readline
from collections import deque

def oper(board, x, y):
    ret = copy.deepcopy(board)
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            if ret[ny][nx] == '.':
                ret[ny][nx] = '*'
            else:
                ret[ny][nx] = '.'
    return ret

def check(arr1, arr2):
    for y in range(3):
        for x in range(3):
            if arr1[y][x] != arr2[y][x]:
                return False
    return True

def binary_board(board):
    ret = ''
    for y in range(3):
        for x in range(3):
            ret += '0' if board[y][x] == '.' else '1'

    return int(ret, 2)

def bfs(board):
    q = deque()
    s = [['.' for _ in range(3)] for _ in range(3)]
    q.append(s)
    visit = [0 for _ in range(1000)]
    time = 0
    visit[binary_board(s)] = 1

    while q:
        length = len(q)
        while length:
            now = q.popleft()

            if check(now, board):
                return time
            for y in range(3):
                for x in range(3):
                    oper_board = oper(now, x, y)
                    b = binary_board(oper_board)
                    if not visit[b]:
                        q.append(oper_board)
                        visit[b] = 1
            length -= 1
        time += 1

dx = [0, -1, 0, 1, 0]
dy = [0, 0, -1, 0, 1]

p = int(input())

for _ in range(p):
    board = []
    for i in range(3):
        board.append(list(input()))

    print(bfs(board))