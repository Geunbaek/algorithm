import sys
input = sys.stdin.readline

expression = '(' + input().strip() + ')'
priority = {
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2,
    "(" : 0,
}
ans = ''
stack = []

for e in expression:
    if e.isalpha():
        ans += e
    elif e == '(':
        stack.append(e)
    elif e == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
    else:
        while stack and stack[-1] != '(' and priority[e] <= priority[stack[-1]]:
            ans += stack.pop()
        stack.append(e)
while stack:
    ans += stack.pop()
print(ans)
