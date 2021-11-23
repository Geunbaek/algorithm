import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ans = 0

while bin(n).count('1') > k:
    temp = bin(n)
    idx = len(bin(n)) - temp.rindex('1') -1
    ans += 2 ** idx
    n += 2 ** idx

print(ans)