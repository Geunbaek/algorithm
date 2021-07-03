import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    q = set()
    q.add((0, 0, board[0][0]))
    cnt = 1

    while q:
        x, y, path = q.pop()

        if cnt < len(path):
            cnt = len(path)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if board[ny][nx] not in path:
                    q.add((nx, ny, path + board[ny][nx]))
    return cnt

r, c = map(int, input().split())
board = []

for _ in range(r):
    board.append(list(map(str,input().strip())))

print(bfs())