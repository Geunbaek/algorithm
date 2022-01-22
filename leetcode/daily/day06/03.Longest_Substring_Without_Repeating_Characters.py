class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = dict()
        start = 0
        length = 0
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                length = max(length, idx - start + 1)
            used[char] = idx

        return length
