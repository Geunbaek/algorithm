import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    arr_b.sort()
    cnt = 0

    for el in arr_a:
        l = 0
        r = m - 1
        while l <= r:
            mid = (l + r) // 2
            if arr_b[mid] < el:
                l = mid + 1
            else:
                r = mid - 1
        cnt += r + 1
    print(cnt)

