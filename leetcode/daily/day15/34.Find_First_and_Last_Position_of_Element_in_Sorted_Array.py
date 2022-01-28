from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        ans = []
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        ans.append(left)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        ans.append(right)

        for i in range(len(ans)):
            if ans[i] < 0 or ans[i] >= len(nums) or nums[ans[i]] != target:
                ans[i] = -1

        return ans

sol = Solution()
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8))

