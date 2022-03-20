from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_length = 0
        for i in range(len(nums)):
            if max_length < i :
                return False
            max_length = max(max_length, i + nums[i])
        return True
