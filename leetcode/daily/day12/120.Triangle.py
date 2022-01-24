from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(el))] for el in triangle]
        dp[0][0] = triangle[0][0]

        for y in range(1, len(triangle)):
            for x in range(len(triangle[y])):
                if x == 0:
                    dp[y][x] = dp[y-1][x] + triangle[y][x]
                elif x == len(triangle[y]) - 1:
                    dp[y][x] = dp[y-1][x - 1] + triangle[y][x]
                else:
                    dp[y][x] = min(dp[y-1][x-1], dp[y-1][x]) + triangle[y][x]

        return min(dp[-1])