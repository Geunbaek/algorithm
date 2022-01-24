class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        binary = bin(n)
        if binary.count('1') == 1:
            return True
        return False


