import sys
input = sys.stdin.readline
from collections import deque
import heapq

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(start, current_size):
    q = deque()
    q.append(start)

    cur_x, cur_y, cnt = start
    board[cur_y][cur_x] = 0

    visit = set()
    fishes = []

    while q:
        x, y, cnt = q.popleft()
        visit.add((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visit:
                visit.add((nx, ny))
                if board[ny][nx] == 0 or board[ny][nx] == current_size:
                    q.append((nx, ny, cnt+1))
                    continue

                if board[ny][nx] > current_size:
                    continue
                else:
                    heapq.heappush(fishes, (cnt+1, ny, nx))
    if fishes:
        return fishes[0]
    else:
        return None


n = int(input())
board = []
current_size = 2
time = 0
eating_cnt = 0

for y in range(n):
    line = list(map(int, input().split()))
    for x in range(len(line)):
        if line[x] == 9:
            position = (x, y, 0)
    board.append(line)

while True:
    next_fish = bfs(position, current_size)

    if next_fish is None:
        break

    cnt, ny, nx = next_fish
    time += cnt

    eating_cnt += 1

    if current_size == eating_cnt:
        current_size += 1
        eating_cnt = 0

    position = (nx, ny, 0)

print(time)


