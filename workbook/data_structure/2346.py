import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

results = []
index_arr = []

for i in range(1, n+1):
    index_arr.append(i)

index = 0
k = arr.pop(index)
results.append(index_arr.pop(index))

while arr:

    if k < 0:
        index = (index + k) % len(arr)
    else:
        index = (index + (k-1)) % len(arr)

    k = arr.pop(index)
    results.append(index_arr.pop(index))

for i in range(n):
    print(results[i], end = ' ')

