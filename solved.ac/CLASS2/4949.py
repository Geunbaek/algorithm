import sys
input = sys.stdin.readline
import re

while True:
    line = input().rstrip()
    if line == '.':
        break
    line = re.sub(r"[^\[\]()]", "", line)
    stack =[]
    ck = True
    for char in line:
        if char == "[" or char == "(":
            stack.append(char)
        elif char == ']':
            if not stack:
                ck = False
                break
            if stack.pop() != "[":
                ck = False
                break
        elif char == ")":
            if not stack:
                ck = False
                break
            if stack.pop() != "(":
                ck = False
                break
    if stack or not ck :
        print("no")
    else:
        print("yes")

