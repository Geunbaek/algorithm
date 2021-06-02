import sys
input = sys.stdin.readline
import heapq

def solve(start):
    h = []
    distance = [float('inf') for _ in range(v+1)]
    distance[start] =0
    for ne, w in graph[start]:
        heapq.heappush(h, (w, ne))

    while h:
        weight, now = heapq.heappop(h)
        if distance[now] > weight:
            distance[now] = weight
            for ne, w in graph[now]:
                heapq.heappush(h, (weight+w, ne))

    return distance[1:]

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    node_info = list(map(int, input().split()))
    for i in range(1, len(node_info), 2):
        if node_info[i] == -1:
            break
        graph[node_info[0]].append((node_info[i], node_info[i+1]))

ans = solve(1)
node, max_val = 0, 0

for i, val in enumerate(ans):
    if max_val < val:
        node, max_val = i+1, val

ans = solve(node)

print(max(ans))
"""

4
1 2 5 3 9 -1
2 1 5 -1
3 1 9 4 8 -1
4 3 8 -1

22

6
1 2 3 -1
2 1 3 5 3 3 5 -1
3 2 5 4 7 -1
4 3 7 -1
5 2 3 6 5 -1
6 5 5 -1

20
"""
