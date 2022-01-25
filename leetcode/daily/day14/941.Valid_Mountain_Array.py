from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        status = [-1 for _ in range(len(arr) - 1)]
        for idx, el in enumerate(arr[:-1]):
            if arr[idx + 1] > el:
                status[idx] = 1
            elif arr[idx + 1] < el:
                status[idx] = 2
            else:
                return False

        return 1 in status and 2 in status and sorted(status) == status






