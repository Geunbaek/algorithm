from typing import List
from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque()
        q.append((amount, 0))
        visit = set()
        while q:
            now, cnt = q.popleft()
            if now == 0:
                return cnt
            for c in coins:
                if now - c not in visit and now - c >= 0:
                    visit.add(now - c)
                    q.append((now - c, cnt + 1))
        return -1