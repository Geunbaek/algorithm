import sys
input = sys.stdin.readline
import heapq

INF = 10**9

def solve(start):
    h = []
    distance = [INF] * (n+1)
    distance[start] =0
    for c, node in graph[start]:
        heapq.heappush(h, (c, node))

    while h:
        cur_cost, now = heapq.heappop(h)
        if distance[now] > cur_cost:
            distance[now] = cur_cost
            for c, node in graph[now]:
                heapq.heappush(h, (cur_cost+c, node))
    return distance[end]

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))

start, end = map(int, input().split())

print(solve(start))
