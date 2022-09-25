from collections import deque
def bfs(graph, info):
    q = deque()
    maxCount = 0
    q.append((0, 0, 0, [0 for i in range(len(info))], []))
    while q:
        node, s, w, visited, nexts = q.popleft()

        if visited[node] == 1:
            continue

        s = s + (1 if info[node] == 0 else 0)
        w = w + (1 if info[node] == 1 else 0)

        if w >= s:
            continue

        visited[node] = 1

        maxCount = max(maxCount, s)

        for _next in nexts + graph[node]:
            q.append((_next, s, w, visited[:], nexts + graph[node]))

    return maxCount


def solution(info, edges):
    graph = [[] for _ in range(len(info))]

    for parent, child in edges:
        graph[parent].append(child)
        graph[child].append(parent)

    return bfs(graph, info)

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))