import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def dfs(depth, cnt):
    if cnt >= m:
        for i in range(len(arr)):
            if arr[i] == 1:
                print(i)
        return

    for i in range(depth, n+1):
        if arr[i] == 0:
            arr[i] = 1
            dfs(i+1, cnt +1)
            arr[i] = 0



n, m = map(int, input().split())
arr = [0 for _ in range(n+1)]

dfs(1, 0)


