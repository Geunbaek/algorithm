from typing import List
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = [0 for _ in range(len(isConnected) + 1)]
        ans = 0

        def bfs(a):
            if visit[a + 1] == 1:
                return 0

            q = deque()
            q.append(a)
            visit[a + 1] = 1
            while q:
                y = q.popleft()
                for idx, ck in enumerate(isConnected[y]):
                    if ck == 1 and visit[idx + 1] == 0:
                        visit[idx + 1] = 1
                        q.append(idx)
            return 1

        for y in range(len(isConnected)):
            ans += bfs(y)
        return ans

