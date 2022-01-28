from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        check = []
        for r in matrix:
            check += r
        left, right = 0, len(check) - 1

        while left <= right:
            mid = (left + right) // 2
            if check[mid] < target:
                left = mid + 1
            elif check[mid] > target:
                right = mid - 1
            else:
                return True
        return False
