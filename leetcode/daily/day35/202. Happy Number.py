class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n != 1:
            if n in visit:
                return 0
            visit.add(n)
            temp = 0
            for num in str(n):
                temp += int(num)** 2
            n = temp
        return 1 if n == 1 else 0
