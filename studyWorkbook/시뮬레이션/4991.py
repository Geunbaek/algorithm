import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def bfs(board, startX, startY, endX, endY):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    moveMove = 0

    width = len(board[0])
    height = len(board)

    visited = [[0 for _ in range(width)] for _ in range(height)]
    visited[startY][startX] = 1

    q = deque([(startX, startY, moveMove)])

    while q:
        x, y, curMove = q.popleft()
        if x == endX and y == endY:
            return curMove

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < width and 0 <= ny < height:
                if board[ny][nx] != 'x' and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((nx, ny, curMove + 1))

    return -1

def dfs(graph, curPos, curCost, depth, visited):
    global answer
    if len(graph) <= depth:
        if answer[-1] == -1:
            answer[-1] = curCost
        else:
            answer[-1] = min(answer[-1], curCost)
        return

    for _, nextPos, cost in graph[curPos]:
        if visited[nextPos] == 0:
            visited[nextPos] = 1
            dfs(graph, nextPos, curCost + cost, depth + 1, visited)
            visited[nextPos] = 0


answer = []
while True:
    flag = True
    w, h = map(int, input().split())
    if not w and not h:
        break

    answer.append(-1)
    board = []
    edgePos = []
    for y in range(h):
        line = list(input().strip())
        board.append(line)
        for x in range(w):
            if line[x] == '*':
                edgePos.append((len(edgePos), x, y))
            elif line[x] == 'o':
                cleanerPosIndex = len(edgePos)
                edgePos.append((len(edgePos), x, y))

    graph = [[] for _ in range(len(edgePos))]

    for start, end in combinations(edgePos, 2):
        startPosIndex, startX, startY = start
        endPosIndex, endX, endY = end
        dist = bfs(board, startX, startY, endX, endY)
        if dist == -1:
            flag = False
            break
        graph[startPosIndex].append((startPosIndex, endPosIndex, dist))
        graph[endPosIndex].append((endPosIndex, startPosIndex, dist))

    if not flag:
        continue

    visited = [0 for _ in range(len(graph))]
    visited[cleanerPosIndex] = 1
    dfs(graph, cleanerPosIndex, 0, 1, visited)

for a in answer:
    print(a)
