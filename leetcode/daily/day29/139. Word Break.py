from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0 for _ in range(len(s))]

        for i in range(len(s)):
            for word in wordDict:
                if word == s[i - len(word) + 1: i + 1]:
                    if dp[i - len(word)] or i - len(word) == -1:
                        dp[i] = 1
        return dp[-1]
