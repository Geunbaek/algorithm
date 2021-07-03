import sys

input = sys.stdin.readline

s = list(map(int, input().split()))
if sorted(s) == s:
    print("ascending")
elif sorted(s, reverse=True) == s:
    print("descending")
else:
    print("mixed")