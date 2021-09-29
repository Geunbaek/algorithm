import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m = map(int, input().split())

def rec(results):
    if len(results) == m:
        print(' '.join(map(str, results)))
        return
    if len(results) == 0:
        for i in range(1, n+1):
            results.append(i)
            rec(results)
            results.pop()
    else:
        for i in range(results[-1], n+1):
            results.append(i)
            rec(results)
            results.pop()

rec([])


