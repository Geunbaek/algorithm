class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = " " + word1
        word2 = " " + word2

        dp = [[0 for _ in range(len(word1))] for _ in range(len(word2))]

        for y in range(len(word2)):
            for x in range(len(word1)):
                if x == 0 or y == 0:
                    dp[y][x] = 0
                elif word1[x] == word2[y]:
                    dp[y][x] = max(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1] + 1)
                else:
                    dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])

        return len(word1) - 1 + len(word2) - 1 - dp[-1][-1] * 2