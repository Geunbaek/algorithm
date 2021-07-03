import sys
input = sys.stdin.readline

n, k = map(int, input().split())
costs = []

for _ in range(n):
    cost = int(input())
    costs.append(cost)

costs.sort(reverse=True)
cnt = 0

for c in costs:
    if k >= c:
        cnt += k // c
        k %= c
    if k == 0:
        break

print(cnt)