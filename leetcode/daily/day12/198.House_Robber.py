from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums.pop()
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], nums[i] + dp[i - 3])

        return max(dp)
