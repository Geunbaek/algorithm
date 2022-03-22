class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        ret = 1
        while n > 4:
            ret *= 3
            n -= 3
        ret *= n
        return ret

sol = Solution()
print(sol.integerBreak(5))