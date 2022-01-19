class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return " ".join(map(lambda x:x[::-1], s))
