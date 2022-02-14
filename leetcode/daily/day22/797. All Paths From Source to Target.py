from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visit = [0 for _ in range(len(graph))]
        ans = []

        def dfs(node, path):
            if node == len(graph) - 1:
                ans.append(path)
                return

            for next_node in graph[node]:
                if visit[next_node] == 0:
                    visit[next_node] = 1
                    dfs(next_node, path + [next_node])
                    visit[next_node] = 0

        visit[0] = 1
        dfs(0, [0])
        return ans
