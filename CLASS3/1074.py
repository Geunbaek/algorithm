import sys
input = sys.stdin.readline

n, r, c = map(int,input().split())
num = 0
while True:
    if n == 1:
        if r == 0 and c == 0:
            break
        if r == 0 and c == 1:
            num += 1
            break
        if r == 1 and c == 0:
            num += 2
            break
        if r == 1 and c == 1:
            num += 3
            break
    else:
        if 2**(n-1) > r and 2 **(n-1) > c:
            n -= 1
        elif 2**(n-1) > r and 2 **(n-1) <= c:
            num += 2**(n-1) * 2**(n-1)
            c %= 2**(n-1)
            n -= 1
        elif 2**(n-1) <= r and 2**(n-1) > c:
            num += 2 * (2 ** (n - 1) * 2 ** (n - 1))
            r %= 2**(n-1)
            n -= 1
        elif 2**(n-1) <= r and 2**(n-1) <= c:
            num += 3 * (2 ** (n - 1) * 2 ** (n - 1))
            c %= 2 ** (n - 1)
            r %= 2 ** (n - 1)
            n -= 1

print(num)

