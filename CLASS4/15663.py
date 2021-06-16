import sys
input = sys.stdin.readline

def dfs(depth):
    if depth == m:
        results.append(result[:])
        return

    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            result[depth] = arr[i]
            dfs(depth + 1)
            visit[i] = 0
            result[depth] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
visit = [0 for _ in range(n)]
result = [0 for _ in range(m)]
results = []

dfs(0)
results.sort()
print(' '.join(map(str, results[0])))
for i in range(1, len(results)):
    if results[i] != results[i-1]:
        print(' '.join(map(str, results[i])))

