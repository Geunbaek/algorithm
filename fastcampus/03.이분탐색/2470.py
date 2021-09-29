import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = sys.maxsize
val = []
arr.sort()
for idx, el in enumerate(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if el + arr[mid] < 0:
            left = mid + 1
            if abs(el + arr[mid]) < ans:
                if mid == idx:
                    continue
                ans = abs(el + arr[mid])
                val = [el, arr[mid]]
        else:
            right = mid - 1
            if abs(el + arr[mid]) < ans:
                if mid == idx:
                    continue
                ans = abs(el + arr[mid])
                val = [el, arr[mid]]

val.sort()
print(val[0], val[1])
