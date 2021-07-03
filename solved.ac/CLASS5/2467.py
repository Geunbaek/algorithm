import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

d = float('inf')
results = []

for i in range(n):
    left, right = i+1, n - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[i] + arr[mid] < 0:
            left = mid + 1
        elif arr[i] + arr[mid] > 0:
            right = mid - 1
        else:
            results.append((arr[i], arr[mid]))
            break

        if d > abs(arr[i] + arr[mid]):
            d = abs(arr[i] + arr[mid])
            results.append((arr[i], arr[mid]))

results.sort(key = lambda x: (abs(x[0]+x[1])))

print(results[0][0], results[0][1])





