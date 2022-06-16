import sys
input = sys.stdin.readline

def dfs(x, y, now):
    global max_ans, min_ans
    if x == n - 1 and y == n - 1:
        max_ans = max(max_ans, int(now[0]))
        min_ans = min(min_ans, int(now[0]))
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if board[ny][nx].isdigit():
                    dfs(nx, ny, [oper(now[0], board[ny][nx], now[1])])
                else:
                    dfs(nx, ny, now + [board[ny][nx]])
                visited[ny][nx] = 0

def oper(a, b, op):
    a = int(a)
    b = int(b)
    if op == "+":
        return a + b
    elif op == '-':
        return a - b
    elif op == "*":
        return a * b


n = int(input())
board = []
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [1, 0]
dy = [0, 1]


for _ in range(n):
    line = input().strip().split()
    board.append(line)

max_ans = -sys.maxsize
min_ans = sys.maxsize
visited[0][0] = 1
dfs(0, 0,[board[0][0]])
print(max_ans, min_ans)

