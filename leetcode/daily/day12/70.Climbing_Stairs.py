class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        if n >= 2:
            dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i] + dp[i - 1]
        return dp[n]
