import heapq

INF = float("inf")


def dij(start, graph):
    dist = [INF for _ in range(len(graph))]
    h = []
    heapq.heappush(h, (0, start))

    while h:
        curCost, now = heapq.heappop(h)
        if dist[now] > curCost:
            dist[now] = curCost
            for _next, cost in graph[now]:
                if curCost + cost < dist[_next]:
                    heapq.heappush(h, (curCost + cost, _next))
    return dist[1:]


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]

    for x, y, c in fares:
        graph[x].append((y, c))
        graph[y].append((x, c))

    dist = dij(s, graph)
    _min = float("inf")
    for i in range(n):
        totalDist = dist[i]
        aDist = dij(i + 1, graph)
        bDist = dij(i + 1, graph)
        totalDist += aDist[a - 1] + bDist[b - 1]
        _min = min(_min, totalDist)

    return _min