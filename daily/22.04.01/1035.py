import sys
input = sys.stdin.readline
from collections import deque

board = []
pos = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = set()

def pos_to_str(p):
    sorted_p = sorted(p)
    ret = ""
    for x, y in sorted_p:
        ret += f"{x}{y}"
    return ret


for y in range(5):
    line = list(input().strip())
    board.append(line)
    for x in range(5):
        if line[x] == '*':
            pos.append((x, y))
pos_cnt = len(pos)

def check(p):
    a, b = p[0]
    q = deque()
    q.append((a, b))
    visit = set()
    visit.add((a, b))
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if (nx, ny) not in visit and (nx, ny) in p:
                    visit.add((nx, ny))
                    cnt += 1
                    q.append((nx, ny))
    return cnt == pos_cnt

q = deque()
q.append([pos, 0])
visited.add(pos_to_str(pos))

while q:
    pieces, cnt = q.popleft()
    if check(pieces):
        print(cnt)
        break

    for i in range(len(pieces)):
        x, y = pieces[i]
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if (nx, ny) in pieces:
                    continue
                new_p = []
                for k in range(len(pieces)):
                    if k != i:
                        new_p.append(pieces[k])
                    else:
                        new_p.append((nx, ny))

                state = pos_to_str(new_p)
                if state not in visited:
                    visited.add(state)
                    q.append([new_p, cnt + 1])
