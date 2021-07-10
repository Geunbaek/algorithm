import sys

input = sys.stdin.readline

n = int(input())
stack = []
ans = 0

for _ in range(n):
    x, y = map(int, input().split())
    if not stack:
        stack.append(y)
    else:
        ck = []
        while stack and stack[-1] > y:
            elem = stack.pop()
            if elem != 0:
                ck.append(elem)
        stack.append(y)
        if ck:
            ans += len(set(ck))

if 0 in stack:
    ans += len(set(stack)) - 1
else:
    ans += len(set(stack))


print(ans)
