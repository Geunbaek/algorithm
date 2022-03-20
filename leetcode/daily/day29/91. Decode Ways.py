
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        alpha = {str(i - 64) : chr(i) for i in range(65, 65 + 26)}
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            if s[i] in alpha:
                dp[i + 1] += dp[i]
            if i < len(s) and s[i - 1 : i + 1] in alpha:
                dp[i + 1] += dp[i - 1]
        return dp[len(s)]
sol = Solution()
print(sol.numDecodings("111111111111111111111111111111111111111111111"))
