import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

for idx in range(len(arr)):
    arr[idx] **= 2
print(sum(arr)%10)