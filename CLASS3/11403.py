import sys
input = sys.stdin.readline
import heapq

def solve(node):
    h = []
    is_available = [0 for _ in range(n)]
    distance = [float('inf') for _ in range(n)]

    for idx in range(len(graph[node])):
        if graph[node][idx] == 1:
            heapq.heappush(h, (1, idx))

    while h:
        w, now = heapq.heappop(h)
        if distance[now] > w:
            distance[now] = w
            is_available[now] = 1
            for idx in range(len(graph[now])):
                if graph[now][idx] == 1:
                    heapq.heappush(h, (w+1, idx))
    return is_available



n = int(input())
graph = []
board = []


for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    ck = solve(i)
    board.append(ck)

for y in range(n):
    for x in range(n):
        print(board[y][x], end = ' ')
    print()