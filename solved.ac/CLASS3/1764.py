import sys
input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())
name_dict = defaultdict(int)
ans = []

for _ in range(n):
    name = input().strip()
    name_dict[name] += 1

for _ in range(m):
    name = input().strip()
    name_dict[name] += 1

for key, val in name_dict.items():
    if val == 2:
        ans.append(key)

print(len(ans))
ans.sort()
for i in ans:
    print(i)

