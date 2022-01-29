from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                ans.append([start, end])
            if end >= firstList[i][1]:
                i += 1
            if end >= secondList[j][1]:
                j += 1
        return ans




sol = Solution()
print(sol.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))
