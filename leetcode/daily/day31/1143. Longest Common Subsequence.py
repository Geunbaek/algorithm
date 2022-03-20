class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
        text1 = " " + text1
        text2 = " " + text2
        for y in range(1, len(dp)):
            for x in range(1, len(dp[y])):
                if x == 0 or y == 0:
                    dp[y][x] = 0
                else:
                    if text1[x] == text2[y]:
                        dp[y][x] = max(dp[y-1][x -1] + 1, dp[y][x-1], dp[y-1][x])
                    else:
                        dp[y][x] = max(dp[y - 1][x], dp[y][x - 1] )
        return dp[-1][-1]
