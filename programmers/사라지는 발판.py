from collections import deque
import copy


def play(board, aloc, bloc):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    boardState = [[1 for _ in range(len(board[0]))] for _ in range(len(board))]
    q = deque()
    q.append((0, boardState, aloc, bloc, 'A'))

    while q:
        count, bs, a, b, turn = q.popleft()
        if bs[a[0]][a[1]] == 0:
            return count
        if bs[b[0]][b[1]] == 0:
            return count

        if turn == 'A':
            x, y = a
        else:
            x, y = b

        flag = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
                newBoardState = copy.deepcopy(bs)
                if newBoardState[ny][nx] == 1:
                    newBoardState[ny][nx] = 0
                    flag = False
                    if turn == 'A':
                        q.append((count + 1, newBoardState, [nx, ny], b, 'B'))
                    else:
                        q.append((count + 1, newBoardState, a, [nx, ny], 'A'))
        if flag:
            return count


def solution(board, aloc, bloc):
    return play(board, aloc, bloc)

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],	[1, 0],	[1, 2]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]],	[1, 0],	[1, 2]))
print(solution([[1, 1, 1, 1, 1]],	[0, 0],	[0, 4]))
print(solution([[1]],	[0, 0],	[0, 0]))