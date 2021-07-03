import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    idx_arr = []
    answer = 0
    for idx, elem in enumerate(arr):
        idx_arr.append((idx, elem))

    cnt = 0
    while idx_arr:
        max_val = max(idx_arr, key=lambda x:x[1])[1]

        while idx_arr[0][1] < max_val:
            idx_arr.append(idx_arr.pop(0))

        while idx_arr[0][1] == max_val:
            elem = idx_arr.pop(0)
            cnt += 1
            if elem[0] == m:
                answer = cnt
                break
        if answer:
            break
    print(answer)