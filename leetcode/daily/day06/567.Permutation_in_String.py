class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        cnt = {}
        for char in s1:
            cnt[char] = cnt.get(char, 0) + 1

        for i in range(0, len(s2) - length + 1):
            h = {}
            for j in range(i, i + length):
                if s2[j] in cnt and cnt[s2[j]] > h.get(s2[j], 0):
                    h[s2[j]] = h.get(s2[j], 0) + 1
                else:
                    break

            if h == cnt:
                return True
        return False





sol = Solution()
sol.checkInclusion("ab","eidbaooo")


