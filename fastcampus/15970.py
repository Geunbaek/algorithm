import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
position = defaultdict(list)
length = 0

for _ in range(n):
    pos, col = map(int, input().split())
    position[col].append(pos)

for key in position.keys():
    position[key].sort()

for key in position.keys():
    for i in range(len(position[key])):
        if i == 0:
            length += position[key][i+1] - position[key][i]
        elif i == len(position[key]) - 1:
            length += position[key][i] - position[key][i - 1]
        else:
            length += min(position[key][i] - position[key][i - 1], position[key][i+1] - position[key][i])


print(length)