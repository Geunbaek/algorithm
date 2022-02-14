from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        paths = []
        def recur(total, path, idx):
            if total == target and path not in paths:
                paths.append(path)
                return
            elif total > target:
                return

            for i in range(idx, len(candidates)):
                recur(total + candidates[i], path + [candidates[i]], i)

        recur(0, [])
        return paths