import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
arr.sort()
cnt = Counter(arr).most_common()
most = []
most_val = 0
print(cnt)
for elem, c in cnt:
    if c == cnt[0][1]:
        most.append(elem)
most.sort()
if len(most) >= 2:
    most_val = most[1]
else:
    most_val = most[0]

print("%0.f"% (sum(arr)/n))
print(arr[len(arr)//2])
print(most_val)
print(arr[-1]-arr[0])
