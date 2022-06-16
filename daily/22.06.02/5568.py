import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
k = int(input())
card = []
nums = set()

for _ in range(n):
    card.append(input().strip())

for el in permutations(card, k):
    nums.add("".join(el))

print(len(nums))
