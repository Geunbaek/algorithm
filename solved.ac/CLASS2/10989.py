import sys
input = sys.stdin.readline

n = int(input())
num_arr = [0 for _ in range(10000)]
for _ in range(n):
    num = int(input())
    num_arr[num] += 1

for idx in range(len(num_arr)):
    for cnt in range(num_arr[idx]):
        print(idx)
