import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
arr.sort()
for elem in arr:
    print(elem)