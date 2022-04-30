import sys
import time

input = sys.stdin.readline
import copy
from collections import deque

def get_maze_order(depth, path):
    if depth >= 5:
        maze_orders.add(path)

    for i in range(5):
        if checked[i] == 0:
            checked[i] = 1
            get_maze_order(depth + 1, path + f"{i}")
            checked[i] = 0

def rotation(index):
    ret = []
    for x in range(5):
        ret.append([])
        for y in range(4, -1, -1):
            ret[-1].append(maze[index][y][x])
    return ret

def bfs(maze):
    if maze[0][0][0] == 0:
        return 0
    if maze[4][4][4] == 0:
        return 0
    visit = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append((0, 0, 0, 0))
    visit[0][0][0] = 1

    while q:
        x, y, z, cnt = q.popleft()
        if z == 4 and y == 4 and x == 4:
            return cnt

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5:
                if maze[nz][ny][nx] == 1 and visit[nz][ny][nx] == 0:
                    visit[nz][ny][nx] = 1
                    q.append((nx, ny, nz, cnt + 1))

    return 0

start = time.time()
board = []
mazes = set()
maze_orders = set()
checked = [0 for _ in range(5)]

ans = []
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for _ in range(5):
    board.append([])
    for _ in range(5):
        board[-1].append(list(map(int, input().split())))

get_maze_order(0, "")

for order in maze_orders:
    maze = []
    for index in order:
        maze.append(copy.deepcopy(board[int(index)]))

    for first in range(4):
        if first != 0:
            maze[0] = rotation(0)
        for second in range(4):
            if second != 0:
                maze[1] = rotation(1)
            for third in range(4):
                if third != 0:
                    maze[2] = rotation(2)
                for forth in range(4):
                    if forth != 0:
                        maze[3] = rotation(3)
                    for fifth in range(4):
                        if forth != 0:
                            maze[4] = rotation(4)
                        result = bfs(maze)
                        if result != 0:
                            ans.append(result)

if ans:
    print(min(ans))
else:
    print(-1)
