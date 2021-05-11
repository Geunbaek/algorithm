import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    s = input().strip()
    arr.append(s)
arr = list(set(arr))
arr.sort(key = lambda x:(len(x), x))
for elem in arr:
    print(elem)