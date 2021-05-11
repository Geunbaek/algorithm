import sys

input = sys.stdin.readline

k, n = map(int, input().split())
arr = []

for _ in range(k):
    line = int(input())
    arr.append(line)

min_cm = 1
max_cm = max(arr)
answer = 0

while min_cm <= max_cm:
    mid = (min_cm + max_cm) // 2

    cnt = 0
    for elem in arr:
        cnt += elem // mid

    if cnt >= n:
        min_cm = mid + 1
        answer = max(answer, mid)
    else:
        max_cm = mid - 1

print(answer)


