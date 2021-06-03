import sys
input = sys.stdin.readline

INF = 10**9
# bellman ford
def solve2(start):
    dist = [INF] * (n+1)
    dist[start] = 0

    for i in range(n):
        for edge in graph:
            cur = edge[0]
            next_node = edge[1]
            cost = edge[2]
            if dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == n-1:
                    return True
    return False

t = int(input())

for _ in range(t):
    n, m, w = map(int, input().split())
    graph = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))

    ans = solve2(1)

    if ans:
        print('YES')
    else:
        print('NO')