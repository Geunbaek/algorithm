def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for u, v in edges:
        graph[u].append(v)
    ret = 0

    def dfs(sheep, wolf, cur, path):
        nonlocal ret

        if info[cur] == 1:
            wolf += 1
        elif info[cur] == 0:
            sheep += 1

        if sheep <= wolf:
            return

        ret = max(ret, sheep)

        for el in path:
            for next_node in graph[el]:
                if next_node not in path:
                    dfs(sheep, wolf, next_node, path + [next_node])

    dfs(0, 0, 0, [0])
    return ret

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))


