import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr_b = list(map(int, input().split()))
card_count = defaultdict(int)

for el in arr:
    card_count[el] += 1

for el in arr_b:
    if el in card_count:
        print(card_count[el], end = ' ')
    else:
        print(0, end = ' ')