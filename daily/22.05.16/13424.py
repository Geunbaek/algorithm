import sys
input = sys.stdin.readline
import heapq

def dij(s):
    h = []
    heapq.heappush(h, (0, s))
    dist = [10**9 for _ in range(n + 1)]

    while h:
        total, now = heapq.heappop(h)
        if dist[now] > total:
            dist[now] = total
            for _next, cost in graph[now]:
                heapq.heappush(h, (total + cost, _next))
    return dist[1:]

def arr_sum(arr1, arr2):
    temp = []
    for a, b in zip(arr1, arr2):
        temp.append(a + b)
    return temp

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    k = int(input())
    start = list(map(int, input().split()))
    ans = [0 for _ in range(n)]

    for s in start:
        ans = arr_sum(ans, dij(s))

    min_cost = min(ans)
    for i in range(n):
        if ans[i] == min_cost:
            print(i + 1)
            break

