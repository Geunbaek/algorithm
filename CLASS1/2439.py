import sys

input = sys.stdin.readline

N = int(input())

for i in range(N-1, -1, -1):
    print(" "*i + "*"*(N-i))