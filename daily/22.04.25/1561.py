import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

if n < m:
    print(n)
else:
    left, right = 0, 600_000_000_000
    while left <= right:
        mid = (left + right) // 2
        count = m

        for el in arr:
            count += mid // el

        if count < n:
            left = mid + 1
        else:
            right = mid - 1

    count = m
    for el in arr:
        count += right // el

    for index, el in enumerate(arr):
        if (right + 1) % el == 0:
            count += 1

        if count == n:
            print(index + 1)
            break
