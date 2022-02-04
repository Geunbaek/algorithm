from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        ans = 0
        left = 0
        now = 1

        for idx, val in enumerate(nums):
            now *= val
            while left <= idx and now >= k:
                now /= nums[left]
                left += 1
            ans += idx - left + 1

        return ans