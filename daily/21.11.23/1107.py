import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = set(input().strip())

now = 100
num = 10**8

if now == n:
    print(0)
elif m == 10:
    print(abs(n - now))
elif m == 0:
    print(min(len(str(n)), abs(n - now)))
else:
    for i in range(1000000):
        for k in str(i):
            if k in broken:
                break
        else:
            if i == n:
                num = n
                break
            if abs(num - n) > abs(i - n):
                num = i
            else:
                break

    print(min( (len(str(num)) + abs(num - n)), abs(n - now) ))
