import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    temp = list(map(str, input().split()))
    arr.append(temp)

arr.sort(key = lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for el in arr:
    print(el[0])