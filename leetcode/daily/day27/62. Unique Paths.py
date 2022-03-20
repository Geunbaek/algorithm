class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for _ in range(n)] for _ in range(m)]
        for y in range(m):
            for x in range(n):
                if x == 0 or y == 0:
                    paths[y][x] = 1
                else:
                    paths[y][x] = paths[y - 1][x] + paths[y][x - 1]
        return paths[-1][-1]
