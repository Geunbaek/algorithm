from collections import deque
import copy

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(board, a, b, num):
    q = deque()
    oper = [[0,0]]
    q.append((a, b))
    board[b][a] = 2
    while q:
        x, y= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board):
                if board[ny][nx] == num:
                    board[ny][nx] = 2
                    q.append((nx, ny))
                    oper.append([dx[i], dy[i]])
    return oper

def rotate(table, i):
    if not i:
        return table
    new_table = []

    for x in range(len(table)):
        new_table.append([])
        for y in range(len(table)-1, -1, -1):
            new_table[x].append(table[y][x])
    return new_table

def clear(table):
    for y in range(len(table)):
        for x in range(len(table)):
            if table[y][x] == 2:
                table[y][x] = 1

def solution(game_board, table):
    answer = 0

    blocks = []
    for y in range(len(game_board)):
        for x in range(len(game_board)):
            if game_board[y][x] == 0:
                blocks.append(bfs(game_board, x, y, 0))
    print(blocks)
    for i in range(4):
        table = rotate(table, i)
        
        for t in table:
            print(t)
        print()
        for y in range(len(table)):
            for x in range(len(table)):
                if table[y][x] == 1:
                    temp = bfs(table, x, y, 1)

                    if temp in blocks:
                        print(temp)
                        answer += len(temp)
                        blocks.remove(temp)
        clear(table)
    print(answer)
    return answer

solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])