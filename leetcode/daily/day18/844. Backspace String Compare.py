
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def oper(string):
            q = []
            for el in string:
                if el != '#':
                    q.append(el)
                else:
                    if q:
                        q.pop()
            return q
        s1 = oper(s)
        t1 = oper(t)

        return "".join(s1) == "".join(t1)

sol = Solution()
print(sol.backspaceCompare(s = "ab#c", t = "ad#c"))