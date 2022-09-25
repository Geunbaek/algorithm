from collections import deque


def check(place, a, b):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque([(a, b, 0)])
    visited = [[0 for _ in range(5)] for _ in range(5)]
    visited[b][a] = 1

    while q:
        x, y, d = q.popleft()

        if d >= 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if place[ny][nx] == "O" and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((nx, ny, d + 1))
                if place[ny][nx] == 'P' and visited[ny][nx] == 0:
                    return False
    return True


def solution(places):
    answer = []

    for i, place in enumerate(places):
        for y in range(5):
            for x in range(5):
                if place[y][x] == "P":
                    if not check(place, x, y):
                        answer.append(0)
                        break
            if len(answer) - 1 == i:
                break
        if len(answer) - 1 != i:
            answer.append(1)
    return answer