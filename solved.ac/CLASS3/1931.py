import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
room = []
ans = []
for _ in range(n):
    start, end = map(int, input().split())
    room.append((start, end))

room.sort(key=lambda x: (x[1], x[0]))
room = deque(room)

while room:
    ans.append(room.popleft())
    while room and ans[-1][1] > room[0][0]:
        room.popleft()

print(len(ans))

"""
11
1 4
4 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""