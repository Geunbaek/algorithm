import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
print(Counter(arr).most_common()[0][0])
