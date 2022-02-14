from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visit = [0 for _ in range(len(nums))]
        paths = []
        def perm(depth, path):
            if depth >= len(nums):
                if path not in paths:
                    paths.append(path)
                return

            for i in range(len(nums)):
                if visit[i] == 0:
                    visit[i] = 1
                    perm(depth + 1, path + [nums[i]])
                    visit[i] = 0
        perm(0, [])
        return paths

