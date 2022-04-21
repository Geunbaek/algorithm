import sys
input = sys.stdin.readline


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    ap = find(a)
    bp = find(b)
    p[bp] = ap

def get_next(x, y):
    if board[y][x] == 'U':
        nx = x + dx[0]
        ny = y + dy[0]
    elif board[y][x] == 'D':
        nx = x + dx[1]
        ny = y + dy[1]
    elif board[y][x] == 'L':
        nx = x + dx[2]
        ny = y + dy[2]
    elif board[y][x] == 'R':
        nx = x + dx[3]
        ny = y + dy[3]
    if 0 <= nx < m and 0 <= ny < n:
        return nx, ny
    return -1, -1


n, m = map(int, input().split())
board = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
p = [i for i in range(n * m)]

for _ in range(n):
    board.append(list(input().strip()))

for y in range(n):
    for x in range(m):
        nx, ny = get_next(x, y)
        if nx == -1 and ny == -1:
            continue

        if find(ny * m + nx) != find(y * m + x):
            union(ny * m + nx, y * m + x)

count = set()
for el in p:
    count.add(find(el))
print(len(count))





