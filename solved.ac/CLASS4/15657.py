import sys
input = sys.stdin.readline

def dfs(path):
    if len(path) >= m:
        results.append(path[:])
        return

    for i in range(n):
        if not path:
            path.append(arr[i])
            dfs(path)
            path.pop()
        elif path and path[-1] <= arr[i]:
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