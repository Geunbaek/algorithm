import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
arr.sort()

for el in arr_m:
    l = 0
    r = n - 1
    ck = False
    while l <= r:
        mid = (l + r) // 2
        if el < arr[mid]:
            r = mid -1
        elif el > arr[mid]:
            l = mid + 1
        else:
            ck = True
            break
    if ck:
        print(1)
    else:
        print(0)