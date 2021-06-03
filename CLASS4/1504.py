import sys
input = sys.stdin.readline
import heapq

def solve(start):
    h = []
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0
    for w, node in graph[start]:
        heapq.heappush(h, (w, node))
    while h:
        weight, now= heapq.heappop(h)
        if dist[now] > weight:
            dist[now] = weight
            for w, node in graph[now]:
                heapq.heappush(h, (w+weight, node))
    return dist


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())
ans = solve(1)
ans_v1 = solve(v1)
ans_v2 = solve(v2)

val = min(ans[v1] + ans_v1[v2] + ans_v2[n], ans[v2] + ans_v2[v1] + ans_v1[n])
if val == float('inf'):
    print(-1)
else:
    print(val)

