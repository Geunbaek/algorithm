import sys
input = sys.stdin.readline

h, w = map(int, input().split())
arr = list(map(int, input().split()))
stack = []
ans = 0

for i in range(len(arr)):
    while stack and stack[0] <= arr[i]:
        ans += stack[0] - stack.pop()
    stack.append(arr[i])

now = stack.pop()
while len(stack) > 1:
    block = stack.pop()
    if block > now:
        now = block
    else:
        ans += now - block


print(ans)