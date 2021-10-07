import sys
import math
input = sys.stdin.readline

def mul(n, num):
    if num == 1:
        return n
    if num % 2:
        return n * mul(n, num - 1) % mod
    t = mul(n, num // 2)
    return t * t % mod



m = int(input())
ans = 0
mod = 1_000_000_007
for _ in range(m):
    n, s = map(int, input().split())
    g = math.gcd(n, s)
    n //= g
    s //= g
    ans += s * mul(n, mod-2) % mod
    ans %= mod

print(ans)
