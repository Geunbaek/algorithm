from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ck = {}
        for el in p:
            ck[el] = ck.get(el, 0) + 1
        ans = []
        count = {}
        cnt = 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            cnt += 1
            if cnt > len(p):
                cnt -= 1
                count[s[i - len(p)]] = count.get(s[i - len(p)], 0) - 1
                if count[s[i - len(p)]] == 0:
                    del count[s[i - len(p)]]

            if count == ck:
                ans.append(i - len(p) + 1)
        return ans