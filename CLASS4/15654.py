import sys
input = sys.stdin.readline

def dfs(path):
    if len(path)>=m:
        results.append(path[:])
        return

    for i in range(len(arr)):
        if arr[i] not in path:
            path.append(arr[i])
            dfs(path)
            path.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
results = []

dfs([])
results.sort()
for result in results:
    for r in result:
        print(r, end = ' ')
    print()
