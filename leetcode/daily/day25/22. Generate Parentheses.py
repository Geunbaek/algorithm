from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recur(depth, stack, path, count):
            if depth >= n * 2:
                ans.append(path)
                return

            if not stack:
                recur(depth + 1, stack + ["("], path + "(", count - 1)
            else:
                if count:
                    recur(depth + 1, stack[:-1], path + ")", count)
                    recur(depth + 1, stack + ["("], path + "(", count - 1)
                else:
                    recur(depth + 1, stack[:-1], path + ")", count)
        recur(0, [], "", n)
        return ans

