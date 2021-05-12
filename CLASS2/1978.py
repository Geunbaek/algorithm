import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
max_val = max(arr)
check = [True for _ in range(max_val+1)]

for i in range(2, len(check)):
    if check[i]:
        num = i
        while num + i <= len(check)-1:
            num += i
            check[num] = False
cnt = 0
for elem in arr:
    if check[elem] and elem >= 2:
        cnt += 1

print(cnt)