import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
time = 0

for i in range(len(arr)):
    time += sum(arr[:i+1])

print(time)