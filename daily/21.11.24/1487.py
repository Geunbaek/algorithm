import sys
input = sys.stdin.readline

n = int(input())
arr = []
result = {}

for _ in range(n):
    max_cost, d = map(int, input().split())
    arr.append((max_cost, d))

for i in range(len(arr)):
    total = 0
    for j in range(len(arr)):
        if arr[i][0] <= arr[j][0] and arr[i][0] - arr[j][1] >= 0:
            total += arr[i][0] - arr[j][1]
    result[i] = total

ans = sorted(result.items(), key= lambda x : (-x[1], arr[x[0]][0]))
print(arr[ans[0][0]][0] if ans[0][1] else 0)