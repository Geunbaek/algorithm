import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    w, t = map(int, input().split())
    arr.append((w, t))

cnt_dict = {}
for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    cnt_dict[i] = cnt +1
for i in range(n):
    print(cnt_dict[i], end = " ")