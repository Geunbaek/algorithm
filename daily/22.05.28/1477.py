import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)
arr.append(l)
arr = list(set(arr))
arr.sort()
ans = l

left, right = 1, l

while left <= right:
    mid = (left + right) // 2
    count = 0
    for i in range(len(arr) - 1):
        count += (arr[i + 1] - arr[i] - 1) // mid

    if count > m:
        left = mid + 1
    else:
        right = mid - 1

print(left)