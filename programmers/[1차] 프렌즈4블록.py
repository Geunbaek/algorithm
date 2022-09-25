from collections import deque

def removeBlocks(board, deleteBlocks):
    for block in deleteBlocks:
        x, y = block
        board[y][x] = ''

def dropDown(board, r, c):
    y = 0
    while y < c:
        count = r
        x = 0
        while x < r and count > 0:
            while count > 0 and not board[y][x]:
                board[y].pop(x)
                board[y].append('')
                count -= 1
            x += 1
        y += 1

def getDeleteBlocks(board):
    deleteBlocks = set()
    for y in range(len(board) - 1):
        for x in range(len(board[y]) - 1):
            target = board[y][x]
            if not target:
                continue
            if board[y + 1][x] != target:
                continue
            if board[y][x + 1] != target:
                continue
            if board[y + 1][x + 1] != target:
                continue
            deleteBlocks.add((x, y))
            deleteBlocks.add((x + 1, y))
            deleteBlocks.add((x, y + 1))
            deleteBlocks.add((x + 1, y + 1))
    return deleteBlocks

def solution(m, n, board):
    newBoard = []
    totalRemovedBlockCount = 0

    for x in range(n):
        newBoard.append([])
        for y in range(m-1, -1, -1):
            newBoard[-1].append(board[y][x])

    while True:
        deleteBlocks = getDeleteBlocks(newBoard)
        if not deleteBlocks:
            break
        totalRemovedBlockCount += len(deleteBlocks)
        removeBlocks(newBoard, deleteBlocks)
        dropDown(newBoard, m, n)

    return totalRemovedBlockCount

print(solution(6,6,	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))