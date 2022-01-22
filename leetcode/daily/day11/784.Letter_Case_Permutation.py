from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ret = []
        def perm(depth, string):
            if depth >= len(s):
                ret.append(string)
                return

            if s[depth].isalpha():
                perm(depth + 1, string + s[depth].upper())
                perm(depth + 1, string + s[depth].lower())
            else:
                perm(depth + 1, string + s[depth])
        perm(0, "")
        return ret