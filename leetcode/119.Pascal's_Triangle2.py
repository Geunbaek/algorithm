from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[] for _ in range(rowIndex)]
        dp[0].append(1)
        for y in range(1, rowIndex):
            for x in range(len(dp[y - 1]) + 1):
                if x == 0:
                    dp[y].append(1)
                elif x == len(dp[y - 1]):
                    dp[y].append(1)
                else:
                    dp[y].append(dp[y - 1][x - 1] + dp[y - 1][x])

        return dp[-1]
