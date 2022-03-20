from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1] for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i][0] == dp[j][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[i][0] == dp[j][0] + 1:
                        dp[i][1] += dp[j][1]
        return dp

sol = Solution()
print(sol.findNumberOfLIS([1,3,5,4,7]))
