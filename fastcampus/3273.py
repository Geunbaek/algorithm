import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
cnt = 0

for el in arr:
    val = x - el
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if val > arr[mid]:
            l = mid + 1
        elif val < arr[mid]:
            r = mid - 1
        else:
            cnt += 1
            break


print(cnt // 2)