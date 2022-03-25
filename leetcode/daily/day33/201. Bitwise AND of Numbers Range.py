class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while right != left:
            right >>= 1
            left >>= 1
            count += 1
        return left << count

sol = Solution()
print(sol.rangeBitwiseAnd(24, 25))