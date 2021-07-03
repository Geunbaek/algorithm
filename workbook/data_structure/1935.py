import sys

input = sys.stdin.readline

n = int(input())
oper = input().strip()
alpha_val = {}
stack = []

for i in range(n):
    alpha_val[chr(ord('A') + i)] = input().strip()

for op in oper:
    if op.isalpha():
        stack.append(alpha_val[op])
    else:
        elem = stack.pop()
        elem2 = stack.pop()
        stack.append('(' + elem2 + op + elem + ')')

print("%.2f" % eval(stack[0]))
