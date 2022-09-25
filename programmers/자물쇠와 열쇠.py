import copy


def getRotatedBoard(board):
    rotatedBoard = []
    for x in range(len(board[0])):
        rotatedBoard.append([])
        for y in range(len(board) - 1, -1, -1):
            rotatedBoard[-1].append(board[y][x])
    return rotatedBoard


def isVaildKey(board, a, b, key, checkPos):
    visited = copy.deepcopy(board)
    for y in range(len(key)):
        for x in range(len(key[y])):
            if visited[y + b][x + a] == 0 and key[y][x] == 1:
                visited[y + b][x + a] = 1
            elif key[y][x] == 1 and visited[y + b][x + a] == 1:
                return False

    for x, y in checkPos:
        if visited[y][x] == 0:
            return False
    return True


def solution(key, lock):
    board = [[0 for _ in range(60)] for _ in range(60)]
    checkPos = []

    for y in range(20, 20 + len(lock)):
        for x in range(20, 20 + len(lock[y - 20])):
            if lock[y - 20][x - 20] == 0:
                checkPos.append((x, y))
            board[y][x] = lock[y - 20][x - 20]

    rotated1Key = getRotatedBoard(key)
    rotated2Key = getRotatedBoard(rotated1Key)
    rotated3Key = getRotatedBoard(rotated2Key)
    keys = [key, rotated1Key, rotated2Key, rotated3Key]

    for y in range(20 - len(key), 20 + len(lock) + 1):
        for x in range(20 - len(key), 20 + len(lock) + 1):
            for k in keys:
                if isVaildKey(board, x, y, k, checkPos):
                    return True

    return False