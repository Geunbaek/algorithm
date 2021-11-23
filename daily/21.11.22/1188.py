import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

g = math.gcd(n, m)

print(m-g)