import sys
input = sys.stdin.readline

alpha_dict = {
    'a': 'a', 'b': 'b', 'k': 'c', 'd': 'd',
    'e': 'e', 'g': 'f', 'h': 'g', 'i': 'h',
    'l': 'i', 'm': 'j', 'n': 'k', 'ng': 'l',
    'o': 'm', 'p': 'n', 'r': 'o', 's': 'p',
    't': 'q', 'u': 'r', 'w': 's', 'y': 't'
}

def oper(string):
    ret = ""
    idx = 0
    while idx < len(string):
        if idx + 1 < len(string) and string[idx] == "n" and string[idx + 1] == "g":
            ret += alpha_dict["ng"]
        else:
            ret += alpha_dict[string[idx]]
        idx += 1
    return ret

n = int(input())
ans = []

for _ in range(n):
    ans.append(input().strip())

ans.sort(key = lambda x: oper(x))

for a in ans:
    print(a)

