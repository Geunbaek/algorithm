import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = []
elem_arr= []
ck = [0 for _ in range(n)]

for idx, elem in enumerate(list(map(int, input().split()))):
    arr.append((idx, elem))
    elem_arr.append(elem)

arr.sort(key = lambda x :x[1], reverse=True)
elem_arr = set(elem_arr)
arr = deque(arr)
now = []

while arr:
    elem = arr.popleft()
    if elem[1] in elem_arr:
        elem_arr.remove(elem[1])
    ck[elem[0]] = len(elem_arr)

for c in ck:
    print(c, end = ' ')





