import sys
input = sys.stdin.readline

k = int(input())
stack = []
for _ in range(k):
    money = int(input())
    if money != 0:
        stack.append(money)
    else:
        stack.pop()

print(sum(stack))
