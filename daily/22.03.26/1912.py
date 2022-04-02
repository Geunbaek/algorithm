import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

results = [arr[0]]

for i in range(n - 1):
   results.append(max(results[i] + arr[i +1], arr[i + 1]))
print(max(results))
