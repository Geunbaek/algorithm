import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().strip()
    command_info = command.split()

    if len(command_info) == 1:
        if command_info[0] == 'pop':
            if not stack:
                print(-1)
            else:
                print(stack.pop())
        elif command_info[0] == 'size':
            print(len(stack))
        elif command_info[0] == "empty":
            if not stack:
                print(1)
            else:
                print(0)
        elif command_info[0] == "top":
            if not stack:
                print(-1)
            else:
                print(stack[-1])
    else:
        stack.append(command_info[1])

