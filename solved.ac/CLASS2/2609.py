import sys
input = sys.stdin.readline

def gcd(a, b):
    tmp = a % b
    while tmp > 0:
        a = b
        b = tmp
        tmp = a % b
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))

