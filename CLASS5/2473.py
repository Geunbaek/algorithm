import sys
input = sys.stdin.readline
# pypy

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
three_sum = sys.maxsize
ans = []
state = False

for left in range(len(arr)):
    for right in range(left + 2, len(arr)):
        l, r = left, right
        while l <= r:
            mid = (l + r) // 2

            if left == mid or right == mid:
                break

            if abs(arr[left] + arr[right] + arr[mid]) < three_sum:
                ans = [arr[left], arr[mid], arr[right]]
                three_sum = abs(arr[left] + arr[right] + arr[mid])

            if arr[left] + arr[right] + arr[mid] < 0:
                l = mid + 1
            elif arr[left] + arr[right] + arr[mid] > 0:
                r = mid - 1
            else:
                ans = [arr[left], arr[mid], arr[right]]
                state = True
                break

        if state:
            for a in ans:
                print(a, end=' ')
            exit()

for a in ans:
    print(a, end = ' ')

