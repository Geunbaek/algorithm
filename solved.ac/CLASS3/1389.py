import sys
input = sys.stdin.readline
import heapq

def solve(start):
    h = []
    heapq.heappush(h, (0, start))
    distance = [float("inf") for i in range(n + 1)]
    # distance[start] = 0
    # for next_node in graph[start]:
    #     heapq.heappush(h, (1, next_node))

    while h:
        w, now = heapq.heappop(h)
        if distance[now] > w:
            distance[now] = w
            for next_node in graph[now]:
                if distance[next_node] > w + 1:
                    heapq.heappush(h, (w+1, next_node))
    return distance[1:]



n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
min_cost = 10 ** 8
min_person = 0
for i in range(1, n+1):
    ans = solve(i)
    if min_cost > sum(ans):
        min_cost = sum(ans)
        min_person = i

print(min_person)