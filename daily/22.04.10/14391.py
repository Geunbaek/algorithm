import sys
input = sys.stdin.readline
from collections import deque
import copy

def oper(x, y, d, count, visited, num):
    ret = ""
    for j in range(count):
        nx = x + dx[d] * j
        ny = y + dy[d] * j
        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0:
            visited[ny][nx] = num
            ret += board[ny][nx]
        else:
            return ""

    return int(ret) if ret != "" else 0

def check_visit(v):
    for y in range(n):
        if v[y].count(0):
            return False
    return True

def arr_to_str(v):
    ret = ""
    for y in range(n):
        ret += "".join(map(str, v[y]))
    return ret

dx = [1, 0]
dy = [0, 1]

n, m = map(int, input().split())
board = []
ans = 0
banned = set()

for _ in range(n):
    line = list(input().strip())
    board.append(line)

q = deque()

i = 1
while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    result = oper(0, 0, 0, i, visited, 1)
    if result == "":
        break
    q.append((result, visited, 2))
    i += 1

i = 1
while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    result = oper(0, 0, 1, i, visited, 1)
    if result == "":
        break

    q.append((result, visited, 2))
    i += 1

while q:
    now, visited, num = q.popleft()
    if check_visit(visited):
        ans = max(ans, now)
        continue
    flag = False
    for y in range(n):
        for x in range(m):
            if visited[y][x] == 0:
                flag = True
                i = 1
                while True:
                    v = copy.deepcopy(visited)
                    result = oper(x, y, 0, i, v, num)
                    string = arr_to_str(v)
                    if result == "":
                        break

                    if string in banned:
                        i += 1
                        continue

                    banned.add(string)
                    q.append((now + result, v, num + 1))
                    i += 1
                i = 1
                while True:
                    v = copy.deepcopy(visited)
                    result = oper(x, y, 1, i, v, num)
                    string = arr_to_str(v)
                    if result == "":
                        break

                    if string in banned:
                        i += 1
                        continue
                    banned.add(string)
                    q.append((now + result, v, num + 1))
                    i += 1
            if flag:
                break
        if flag:
            break

print(ans)