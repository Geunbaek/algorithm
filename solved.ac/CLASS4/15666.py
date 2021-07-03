import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(depth, result):
    if depth == m:
        if result not in results:
            results.append(result[:])
        return

    for i in range(n):
        if not result:
            result.append(arr[i])
            dfs(depth+1, result)
            result.pop()
        else:
            if result[-1] <= arr[i]:
                result.append(arr[i])
                dfs(depth + 1, result)
                result.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
results = []

dfs(0, [])
results.sort()

for result in results:
    for r in result:
        print(r, end = ' ')
    print()