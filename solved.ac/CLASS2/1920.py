import sys
input = sys.stdin.readline

n = int(input())
arr = set(list(map(int, input().split())))
m = int(input())
check = list(map(int, input().split()))

for elem in check:
    if elem in arr:
        print(1)
    else:
        print(0)
