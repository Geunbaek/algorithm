import sys
from collections import Counter

input = sys.stdin.readline

s = input().strip().upper()
count = Counter(s).most_common(2)

if len(count) == 1 or count[0][1] != count[1][1]:
    print(count[0][0])
else:
    print("?")

