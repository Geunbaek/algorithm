import sys
input = sys.stdin.readline
import heapq

def dij():
    h = []
    heapq.heappush(h, (0, 0))
    dist = [INF for _ in range(n)]

    while h:
        total, now = heapq.heappop(h)
        if dist[now] > total:
            dist[now] = total
            for next_, cost in graph[now]:
                if next_ != n - 1 and check[next_] == 0:
                    heapq.heappush(h, (total + cost, next_))
                elif next_ == n - 1:
                    heapq.heappush(h, (total + cost, next_))


    return dist[-1]


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
INF = sys.maxsize
check = list(map(int, input().split()))

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))


ans = dij()
if ans == INF:
    print(-1)
else:
    print(ans)