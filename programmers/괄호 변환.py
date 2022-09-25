def splitBalanceString(string):
    counter = {"(": 0, ")": 0}
    for i, char in enumerate(string):
        counter[char] += 1
        if counter['('] == counter[')']:
            return [string[:i + 1], string[i + 1:]]
    return ["", ""]


def isValidString(string):
    stack = []

    for char in string:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True


def getReverseString(string):
    ret = ""
    for char in string:
        if char == ")":
            ret += "("
        else:
            ret += ")"
    return ret


def solution(p):
    if not p:
        return p

    ret = ""
    u, v = splitBalanceString(p)
    if isValidString(u):
        ret += u + solution(v)
    else:
        u = u[1:-1]
        ret += f"({solution(v)}){getReverseString(u)}"

    return ret