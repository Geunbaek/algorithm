import sys
input = sys.stdin.readline

def dfs(depth, path):
    if len(path) >= m:
        for p in path:
            print(p, end = ' ')
        print()
        return
    for i in range(depth, n+1):
        path.append(i)
        dfs(i, path)
        path.pop()


n, m = map(int, input().split())
dfs(1, [])
