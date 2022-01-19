from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = sorted(map(lambda x: x** 2, nums))
        return nums