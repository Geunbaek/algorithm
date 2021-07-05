import sys

input = sys.stdin.readline

board = list(input().strip())
stack = []
ans = 0

for idx, char in enumerate(board):
    if char == '(':
        stack.append((idx, char))
    else:
        if board[idx - 1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
print(ans)
