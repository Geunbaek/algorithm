import sys

input = sys.stdin.readline

class Piece:
    def __init__(self, x, y, d, pieceId):
        self.x = x
        self.y = y
        self.d = d
        self.pieceId = pieceId

    def __repr__(self):
        return f"{self.pieceId}"

    def getInfo(self):
        return (self.x, self.y, self.d, self.pieceId)

def findPieceIndex(arr, pieceId):
    for i in range(len(arr)):
        if arr[i].pieceId == pieceId:
            return i

def operateWhiteBoard(prevX, prevY, nextX, nextY, target):
    pieceIndex = findPieceIndex(position[prevY][prevX], target.pieceId)
    prevState = position[prevY][prevX]
    position[prevY][prevX] = prevState[:pieceIndex]
    for p in prevState[pieceIndex:]:
        p.x = nextX
        p.y = nextY
    position[nextY][nextX].extend(prevState[pieceIndex:])

def operateRedBoard(prevX, prevY, nextX, nextY, target):
    pieceIndex = findPieceIndex(position[prevY][prevX], target.pieceId)
    prevState = position[prevY][prevX]
    position[prevY][prevX] = prevState[:pieceIndex]
    for p in prevState[pieceIndex:]:
        p.x = nextX
        p.y = nextY

    position[nextY][nextX].extend(prevState[pieceIndex:][::-1])

def operateBlueBoard(prevX, prevY, d, target):
    reverseDirection = d - 1 if d % 2 != 0 else d + 1

    nextX, nextY = prevX + dx[reverseDirection], prevY + dy[reverseDirection]
    target.d = reverseDirection

    if not isValidRange(n, nextX, nextY) or board[nextY][nextX] == 2:
        return (prevX, prevY)

    if board[nextY][nextX] == 0:
        operateWhiteBoard(prevX, prevY, nextX, nextY, target)
    elif board[nextY][nextX] == 1:
        operateRedBoard(prevX, prevY, nextX, nextY, target)
    return (nextX, nextY)

def isValidRange(n, x, y):
    return 0 <= x < n and 0 <= y < n

def main():
    turn = 0
    while turn < 1000:
        for p in pieces:
            x, y, d, pieceId = p.getInfo()
            nx = x + dx[d]
            ny = y + dy[d]

            if not isValidRange(n, nx, ny) or board[ny][nx] == 2:
                nx, ny = operateBlueBoard(x, y, d, p)
                if len(position[ny][nx]) >= 4:
                    return turn + 1
                continue

            if board[ny][nx] == 0:
                operateWhiteBoard(x, y, nx, ny, p)
            elif board[ny][nx] == 1:
                operateRedBoard(x, y, nx, ny, p)
            if len(position[ny][nx]) >= 4:
                return turn + 1

        turn += 1
    return -1

n, k = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
board = []
position = [[[] for _ in range(n)] for _ in range(n)]
pieces = [None for _ in range(k)]

for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(k):
    y, x, d = map(int, input().split())
    p = Piece(x - 1, y - 1, d - 1, i + 1)
    position[y - 1][x - 1].append(p)
    pieces[i] = p

print(main())
