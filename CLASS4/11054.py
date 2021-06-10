import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

incre_arr = [1 for _ in range(n)]
decre_arr = [1 for _ in range(n)]


for i in range(n):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            incre_arr[j] = max(incre_arr[j], incre_arr[i]+1)

for i in range(n-1, -1, -1):
    for j in range(i-1, -1, -1):
        if arr[i] < arr[j]:
            decre_arr[j] = max(decre_arr[j], decre_arr[i]+1)

result = 0
for i in range(n):
    result = max(result, incre_arr[i]+decre_arr[i])

print(result-1)
