import sys
input = sys.stdin.readline

n = int(input())
w =0
while n>=0:
    if n % 5 == 0:
        w += n // 5
        break
    else:
        w += 1
        n -= 3

if n < 0:
    print(-1)
else:
    print(w)