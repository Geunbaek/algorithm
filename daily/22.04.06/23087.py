import sys
input = sys.stdin.readline
import heapq

def dij():
    h = []
    dist = [[INF, INF] for _ in range(n + 1)]
    dist[x] = [0, 0]
    path_count = [0 for _ in range(n + 1)]
    path_count[x] = 1

    heapq.heappush(h, (0, x, 0))

    while h:
        total, now, cnt = heapq.heappop(h)
        if dist[now][0] >= total and dist[now][1] >= cnt:
            for node, weight in graph[now]:
                if total + weight < dist[node][0]:
                    dist[node] = [total + weight, cnt + 1]
                    path_count[node] = path_count[now]
                    heapq.heappush(h, (total + weight, node, cnt + 1))

                elif total + weight == dist[node][0] and cnt + 1 < dist[node][1]:
                    dist[node][1] = cnt + 1
                    path_count[node] = path_count[now]
                    heapq.heappush(h, (total + weight, node, cnt + 1))

                elif total + weight == dist[node][0] and cnt + 1 == dist[node][1]:
                    path_count[node] += path_count[now]
                    path_count[node] %= 1_000_000_009

    return dist, path_count

n, m, x, y = map(int, input().split())
INF = sys.maxsize
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

d, count = dij()
if d[y][0] == INF:
    print(-1)
else:
    print(d[y][0])
    print(d[y][1])
    print(count[y])
