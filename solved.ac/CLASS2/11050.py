import sys
input = sys.stdin.readline

n, k = map(int, input().split())
over = n
under = k
if k != 0:
    for i in range(k-1):
        over *= n-1
        n -= 1
        under *= k-1
        k -= 1
    print(over // under)
else:
    print(1)



