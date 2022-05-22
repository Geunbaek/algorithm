import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = sys.maxsize
comb = []

for i in range(n - 1):
    for j in range(i + 1, n):
        if i != j:
            comb.append((arr[i] + arr[j], i, j))

comb.sort()
for i in range(len(comb) - 1):
    pos = set([comb[i][1], comb[i][2], comb[i + 1][1], comb[i + 1][2]])
    if len(pos) == 4:
        ans = min(ans, abs(comb[i][0] - comb[i + 1][0]))

print(ans)