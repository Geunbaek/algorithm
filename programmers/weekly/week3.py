
import copy

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(board, a, b, position, num):
    ret = [position]

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < len(board) and 0<= ny < len(board):
            if board[ny][nx] == num:
                board[ny][nx] = 2
                ret = ret + dfs(board, nx, ny, [position[0] + dx[i], position[1] + dy[i]], num)
    return ret

def rotate(table, i):
    if not i:
        return table
    new_table = []

    for x in range(len(table)):
        new_table.append([])
        for y in range(len(table)-1, -1, -1):
            new_table[x].append(table[y][x])
    return new_table

def solution(game_board, table):
    answer = 0

    blocks = []
    for y in range(len(game_board)):
        for x in range(len(game_board)):
            if game_board[y][x] == 0:
                game_board[y][x] = 2
                blocks.append(dfs(game_board, x, y, [0, 0], 0))

    for i in range(4):
        table = rotate(table, i)
        table_copy = copy.deepcopy(table)
        for y in range(len(table)):
            for x in range(len(table)):
                if table_copy[y][x] == 1:
                    table_copy[y][x] = 2
                    temp = dfs(table_copy, x, y, [0, 0], 1)
                    if temp in blocks:
                        answer += len(temp)
                        blocks.pop(blocks.index(temp))
                        table = copy.deepcopy(table_copy)
                    else:
                        table_copy = copy.deepcopy(table)

    return answer

solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])