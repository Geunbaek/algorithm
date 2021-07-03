import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
num_count = [0 for _ in range(10)]
mul_num = list(map(int, str(A*B*C)))

for n in mul_num:
    num_count[n] += 1

for num in num_count:
    print(num)

