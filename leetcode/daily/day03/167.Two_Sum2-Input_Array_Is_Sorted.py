from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = numbers[left] + numbers[right]
            if mid < target:
                left += 1
            elif mid > target:
                right -= 1
            else:
                return [left, right]
