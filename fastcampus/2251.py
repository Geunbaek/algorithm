import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

a, b, c = map(int, input().split())
results = set()
ans = set()

def dfs(x, y, z):
    if (x, y, z) in results:
        return
    results.add((x, y, z))
    if x == 0:
        ans.add(z)
    if x != 0:
        dfs(0 if z + x <= c else z + x - c, y, z + x if z + x <= c else c)
        dfs(0 if y + x <= b else y + x - b, y + x if y + x <= b else b, z)

    if y != 0:
        dfs(x + y if x + y <= a else a, 0 if x + y <= a else x + y - a, z)
        dfs(x, 0 if z + y <= c else z + y - c, z + y if z + y <= c else c)

    if z != 0:
        dfs(x + z if x + z <= a else a, y, 0 if x + z <= a else x + z - a)
        dfs(x, y + z if y + z <= b else b, 0 if y + z <= b else y + z - b)

dfs(0, 0, c)
ans = sorted(list(ans))
for el in ans:
    print(el, end=' ')
