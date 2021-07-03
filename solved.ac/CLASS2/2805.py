import sys
input = sys.stdin.readline

def binary():
    left = 0
    right = max(arr)
    val = 0

    while left <= right:
        mid = (left + right) // 2
        tree = 0
        for elem in arr:
            if elem > mid:
                tree += elem - mid

        if tree >= m:
            left = mid + 1
            val = max(val, mid)
        else:
            right = mid - 1
    return val

n, m = map(int, input().split())

arr = list(map(int, input().split()))

print(binary())