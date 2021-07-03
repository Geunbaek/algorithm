import sys

input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

for elem in a:
    if elem < x:
        print(elem , end =' ')