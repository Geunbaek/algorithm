import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = set()
results = []

for _ in range(n):
    arr.add(input().strip())

for _ in range(m):
    temp = input().strip()
    if temp in arr:
        results.append(temp)
results.sort()
print(len(results))
for el in results:
    print(el)


