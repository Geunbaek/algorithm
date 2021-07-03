import sys
input = sys.stdin.readline
from collections import deque

string = deque(list(input().strip()))
ban = list(input().strip())
stack = []

while string:
    elem = string.popleft()
    stack.append(elem)

    if stack[len(stack)-len(ban):] == ban:
        for i in range(len(ban)):
            stack.pop()



if not stack:
    print('FRULA')
else:
    print(''.join(stack))






