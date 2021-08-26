import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m = map(int, input().split())

def rec(n, results):
    if len(results) == m:
        print(' '.join(map(str, results)))
        return
    for i in range(1, n+1):
        if i not in results:
          results.append(i)
          rec(n, results)
          results.pop()

rec(n, [])


