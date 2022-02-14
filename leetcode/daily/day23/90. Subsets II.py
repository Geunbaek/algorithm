from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ban = [0 for _ in range(len(nums))]
        paths = []

        def dfs(idx, path):
            if path not in paths:
                paths.append(path)

            for i in range(idx, len(nums)):
                if ban[i] == 0:
                    ban[i] = 1
                    dfs(i, path + [nums[i]])
                    ban[i] = 0

        dfs(0, [])
        return paths
