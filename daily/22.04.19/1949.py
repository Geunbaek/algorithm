import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def recur(node):
    visit[node] = 1
    dp[0][node] = arr[node]
    for next_node in tree[node]:
        if visit[next_node] == 0:
            recur(next_node)
            dp[0][node] += dp[1][next_node]
            dp[1][node] += max(dp[0][next_node], dp[1][next_node])


n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(n + 1)] for _ in range(2)]
tree = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

recur(1)
print(max(dp[0][1], dp[1][1]))