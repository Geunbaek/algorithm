import sys
input = sys.stdin.readline


n = int(input())

for j in range(n):
    line = list(map(int, input().split()))
    if j == 0:
        max_line = line[:]
        min_line = line[:]
    else:
        max_tmp = max_line[:]
        min_tmp = min_line[:]

        for i in range(3):
            if i == 0:
                max_line[i] = line[i] + max(max_tmp[i], max_tmp[i+1])
                min_line[i] = line[i] + min(min_tmp[i], min_tmp[i+1])
            elif i == 1:
                max_line[i] = line[i] + max(max_tmp[i], max_tmp[i + 1], max_tmp[i - 1])
                min_line[i] = line[i] + min(min_tmp[i], min_tmp[i + 1], min_tmp[i - 1])
            elif i == 2:
                max_line[i] = line[i] + max(max_tmp[i], max_tmp[i - 1])
                min_line[i] = line[i] + min(min_tmp[i], min_tmp[i - 1])

print(max(max_line), min(min_line))

