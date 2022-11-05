import sys
from collections import deque
import heapq

input = sys.stdin.readline

def getAreaInfo(a, b, target):
    info = {
        "rainbow": [],
        "basic": []
    }

    q = deque([(a, b)])
    visited = set()
    visited.add((a, b))
    while q:
        x, y = q.popleft()
        if board[y][x] == 0:
            heapq.heappush(info["rainbow"], (y, x))
        else:
            heapq.heappush(info["basic"], (y, x))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if (nx, ny) not in visited and board[ny][nx] in (target, 0):
                visited.add((nx, ny))
                q.append((nx, ny))

    return info

def applyGravity(x, y):
    while True:
        ny = y + 1
        if not (ny < n):
            return
        if board[ny][x] != None:
            return
        board[y][x], board[ny][x] = board[ny][x], board[y][x]
        y = ny

def rotate():
    ret = []

    for x in range(n - 1, -1, -1):
        ret.append([])
        for y in range(n):
            ret[-1].append(board[y][x])

    return ret

n, m = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
score = 0

for _ in range(n):
    board.append(list(map(int, input().split())))

while True:
    infos = []
    for y in range(n):
        for x in range(n):
            if board[y][x] is None:
                continue
            if board[y][x] not in (0, -1):
                info = getAreaInfo(x, y, board[y][x])
                if len(info['basic']) >= 1 and len(info['basic']) + len(info['rainbow']) >= 2:
                    infos.append(info)

    if not infos:
        break

    infos.sort(key = lambda x: (-(len(x["basic"]) + len(x["rainbow"])), -len(x["rainbow"]), -x["basic"][0][0], -x['basic'][0][1]))
    target = infos[0]

    score += (len(target["basic"]) + len(target["rainbow"])) ** 2

    for y, x in target['rainbow'] + target["basic"]:
        board[y][x] = None

    for y in range(n - 1, -1, -1):
        for x in range(n):
            if board[y][x] != -1:
                applyGravity(x, y)

    board = rotate()

    for y in range(n - 1, -1, -1):
        for x in range(n):
            if board[y][x] != -1:
                applyGravity(x, y)

print(score)