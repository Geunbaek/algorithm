import sys

input = sys.stdin.readline

s = input().strip()
arr = [-1 for i in range(26)]

for idx in range(len(s)):
    if arr[ord(s[idx])-ord('a')] == -1:
        arr[ord(s[idx])-ord('a')] = idx

for elem in arr:
    print(elem, end = " ")