from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums = [[num, idx] for idx, num in enumerate(nums)]
        nums.sort(key = lambda x: x[0])

        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[left][0] != target:
            return -1
        return left

