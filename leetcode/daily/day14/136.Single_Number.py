from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = {}
        for n in nums:
            num[n] = num.get(n, 0) + 1
        for key, val in num.items():
            if val == 1:
                return key

