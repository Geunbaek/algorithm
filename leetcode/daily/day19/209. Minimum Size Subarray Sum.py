from typing import List
import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = sys.maxsize
        left = 0
        ans = INF
        now = 0

        for right, num in enumerate(nums):
            now += num
            while now >= target:
                ans = min(ans, right - left + 1)
                now -= nums[left]
                left += 1

        return 0 if ans == INF else ans
