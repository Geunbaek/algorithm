import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binary():
    l, r = 0, max(arr)
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        tree = 0
        for el in arr:
            tree += el - mid if el - mid >= 0 else 0
        if tree < m:
            r = mid - 1
        else:
            l = mid + 1
            ans = max(ans, mid)
    return ans

print(binary())