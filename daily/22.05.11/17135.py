import copy
import sys
input = sys.stdin.readline
from collections import deque, defaultdict

def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def check(*pos):
    q = deque()
    visited = [[[0 for _ in range(len(pos))] for _ in range(m)] for _ in range(n)]

    for i, p in enumerate(pos):
        q.append((p, i))

    dists = defaultdict(list)

    while q:
        now, start_pos = q.popleft()
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                dist = get_dist(pos[start_pos], (nx, ny))
                if visited[ny][nx][start_pos] == 0 and dist <= d:
                    visited[ny][nx][start_pos] = 1
                    if copy_board[ny][nx] == 1:
                        dists[start_pos].append((dist, nx, ny))
                    q.append(((nx, ny), start_pos))

    ret = []
    for vals in dists.values():
        vals.sort(key = lambda x: (x[0], x[1]))
        if vals:
            x, y = vals[0][1:]
            ret.append((x, y))

    return set(ret)

def round(board):
    board.pop()
    board.insert(0, [0 for _ in range(m)])

n, m, d = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = 0

for _ in range(n):
    line = list(map(int, input().split()))
    board.append(line)

arrows = []
for x in range(m):
    arrows.append((x, n))

for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):

            count = 0
            copy_board = copy.deepcopy(board)
            for time in range(n):
                if time != 0:
                    round(copy_board)
                results = check(arrows[i], arrows[j], arrows[k])

                for result in results:
                    copy_board[result[1]][result[0]] = 0
                    count += 1
            ans = max(ans, count)

print(ans)
