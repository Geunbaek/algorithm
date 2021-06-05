import sys
input = sys.stdin.readline
import math

n, m = map(int, input().split())

print(math.factorial(n)//(math.factorial(m)*math.factorial(n-m)))