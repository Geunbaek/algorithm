import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
queue = deque()

for _ in range(n):
    command = input().strip()
    command_info = command.split()

    if len(command_info) == 1:
        if command_info[0] == "pop":
            if not queue:
                print(-1)
            else:
                print(queue.popleft())
        elif command_info[0] == "size":
            print(len(queue))
        elif command_info[0] == "empty":
            if not queue:
                print(1)
            else:
                print(0)
        elif command_info[0] == 'front':
            if not queue:
                print(-1)
            else:
               print(queue[0])
        elif command_info[0] == "back":
            if not queue:
                print(-1)
            else:
                print(queue[-1])
    else:
        queue.append(command_info[1])