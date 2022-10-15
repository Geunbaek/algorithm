import sys
input = sys.stdin.readline

def coveredWithPaper(x, y, size):
    for ny in range(y, y + size):
        for nx in range(x, x + size):
            board[ny][nx] = 0

def uncovedWithPaper(x, y, size):
    for ny in range(y, y + size):
        for nx in range(x, x + size):
            board[ny][nx] = 1

def canCoveredWithPaper(x, y, size):
    for ny in range(y, y + size):
        for nx in range(x, x + size):
            if board[ny][nx] == 0:
                return False
    return True

def main(depth, count, total):
    global answer

    if depth >= 100:
        if total == 0:
            answer = min(answer, count)
        return

    x, y = depth % 10, depth // 10
    if board[y][x] == 0:
        main(depth + 1, count, total)
    else:
        for size in range(5, 0, -1):
            if paperCounter[size] <= 0:
                continue
            if x + size > 10 or y + size > 10:
                continue
            if canCoveredWithPaper(x, y, size):
                coveredWithPaper(x, y, size)
                paperCounter[size] -= 1
                main(depth + 1, count + 1, total - size**2)
                uncovedWithPaper(x, y, size)
                paperCounter[size] += 1

board = []
totalCount = 0
answer = sys.maxsize

for _ in range(10):
    line = list(map(int, input().split()))
    totalCount += line.count(1)
    board.append(line)

paperCounter = [5 for _ in range(6)]

main(0, 0, totalCount)
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
