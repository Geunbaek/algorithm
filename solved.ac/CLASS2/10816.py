import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
num_arr = list(map(int, input().split()))
m = int(input())
check_num = list(map(int, input().split()))
num_cnt_dict = defaultdict(int)

for num in num_arr:
    num_cnt_dict[num] += 1

for num in check_num:
    print(num_cnt_dict[num], end = " ")