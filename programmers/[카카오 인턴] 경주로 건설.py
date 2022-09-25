from collections import deque


def bfs(board):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque([(0, 0, 0, -1)])
    visited = [[[10 ** 9 for _ in range(4)] for _ in range(len(board[0]))] for _ in range(len(board))]
    visited[0][0] = [0, 0, 0, 0]

    while q:
        x, y, cost, d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
                curCost = 100 if d == i or d == -1 else 600
                if board[ny][nx] == 0 and visited[ny][nx][i] > cost + curCost:
                    visited[ny][nx][i] = cost + curCost
                    q.append((nx, ny, cost + curCost, i))

    return min(visited[-1][-1])


def solution(board):
    return bfs(board)