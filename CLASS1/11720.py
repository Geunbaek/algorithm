import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip()))


print(sum(arr))