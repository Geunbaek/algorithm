import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0

for idx, el in enumerate(arr):
    l, r = 0, n-1
    while l < r:
        if l == idx:
            l += 1
        elif r == idx:
            r -= 1

        if l == r:
            break

        if arr[l] + arr[r] < el:
            l += 1
        elif arr[l] + arr[r] > el:
            r -= 1
        else:
            ans += 1
            break
print(ans)