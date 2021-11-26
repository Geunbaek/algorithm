import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set(map(int, input().split()))

min_val = sys.maxsize

for x in range(1, 1002):
    if x in s:
        continue
    for y in range(x, 1002):
        if y in s:
            continue
        for z in range(y, 1002):
            if z in s:
                continue
            min_val = min(min_val, abs(n - x*y*z))

            if x * y * z > n:
                break
print(min_val)
