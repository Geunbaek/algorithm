import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(idx):
    global ans
    visit[idx] = True
    tmp.append(idx)
    num = arr[idx]

    if visit[num]:
        if num in tmp:
            ans += tmp[tmp.index(num):]
        return
    else:
        dfs(num)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visit = [True] + [False] * n
    ans = []

    for i in range(1, n+1):
        if not visit[i]:
            tmp = []
            dfs(i)

    print(n - len(ans))



