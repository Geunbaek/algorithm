import math


def check(n):
    if n == 0 or n == 1: return 0
    if n == 2:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def make_knum(n, k):
    ret = ""
    while n >= k:
        ret = f"{n % k}" + ret
        n //= k

    ret = f"{n}" + ret if n else "" + ret
    return ret


def oper(index, knum):
    if index >= len(knum):
        return 0

    ret = ""
    for i in range(index, len(knum)):
        if knum[i] == "0":
            break
        ret += f"{knum[i]}"
    return int(ret) if ret else 0


def solution(n, k):
    knum = make_knum(n, k)
    ans = 0
    for i in range(len(knum)):
        if i == 0:
            ans += check(oper(i, knum))
            continue
        if knum[i] == "0":
            ans += check(oper(i + 1, knum))

    return ans