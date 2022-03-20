from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        cur, last = 0, 0
        time = 0

        for i in range(len(nums)):
            cur = max(cur, i + nums[i])
            if i == last:
                last = cur
                time += 1
                if cur >= len(nums) - 1:
                    return time
        return time

