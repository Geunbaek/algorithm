from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        sub_arr = 0
        for i in range(len(nums) - 2):
            diff = nums[i + 1] - nums[i]
            for j in range(i + 2, len(nums)):
                if nums[j] - nums[j - 1] == diff:
                    sub_arr += 1
                else:
                    break

        return sub_arr
