class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:].zfill(32)
        return int(n[::-1], 2)



sol = Solution()
print(sol.reverseBits(43261596))

