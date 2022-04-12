import copy
import sys
input = sys.stdin.readline

from collections import deque

def oper(r, b, d, sub_board):
    ret = {}
    temp = [(r, 0), (b, 1)]
    if d == 0:
        temp.sort(key = lambda x: x[0][0])
    elif d == 1:
        temp.sort(key = lambda x: x[0][1])
    elif d == 2:
        temp.sort(key = lambda x: -x[0][0])
    elif d == 3:
        temp.sort(key = lambda x: -x[0][1])

    temp = deque(temp)
    flag = False
    while temp:
        bead, color = temp.popleft()
        x, y = bead
        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < m and 0 <= ny < n:
                if sub_board[ny][nx] == ".":
                    x = nx
                    y = ny
                elif color == 0 and sub_board[ny][nx] == "O":
                    flag = True
                    x = nx
                    y = ny
                    break
                elif color == 1 and sub_board[ny][nx] == "O":
                    return None, False
                else:
                    break
        if color == 0:
            sub_board[r[1]][r[0]] = "."
            if not flag:
                sub_board[y][x] = "R"

        if color == 1:
            sub_board[b[1]][b[0]] = "."
            sub_board[y][x] = "B"

        ret[color] = (x, y)
    return ret, flag

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
board = []

hole = []
pos = {}

for y in range(n):
    line = list(input().strip())
    board.append(line)
    for x in range(m):
        if board[y][x] == 'R':
            pos["R"] = (x, y)
        elif board[y][x] == 'B':
            pos["B"] = (x, y)
        elif board[y][x] == "O":
            hole = [x, y]

q = deque()
q.append((pos['R'], pos['B'], board, 0))
visit = set()
visit.add((pos['R'], pos['B']))

while q:
    red, blue, now_board, cnt = q.popleft()
    for i in range(4):
        copy_board = copy.deepcopy(now_board)
        beads_pos, state = oper(red, blue, i, copy_board)
        if beads_pos is None and not state:
            continue

        if (beads_pos[0], beads_pos[1]) in visit:
            continue
        visit.add((beads_pos[0], beads_pos[1]))
        if state:
            print(cnt + 1)
            exit()
        else:
            q.append((beads_pos[0], beads_pos[1], copy_board, cnt + 1))


print(-1)