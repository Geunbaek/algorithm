import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    line = input().strip()
    stack = []
    ck = True

    for char in line:
        if char == "(":
            stack.append(char)

        if char == ")":
            if not stack:
                ck = False
                break
            if stack.pop() !="(":
                ck = False
                break
    if not ck or stack:
        print("NO")
    else:
        print("YES")
