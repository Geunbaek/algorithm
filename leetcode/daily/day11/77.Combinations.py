from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        visit = [0 for _ in range(n + 1)]
        def comb(depth, path, idx):
            if depth >= k:
                ret.append(path)
                return

            for i in range(idx, n + 1):
                if visit[i] == 0:
                    visit[i] = 1
                    comb(depth + 1, path + [i], idx + 1)
                    visit[i] = 0

        comb(0, [], 1)
        return ret
