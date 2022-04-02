import sys
input = sys.stdin.readline

string = input().strip()

stack = []

for char in string:
    stack.append(char)
    while "".join(stack[-4:]) == "PPAP":
        for i in range(4):
            stack.pop()
        stack.append("P")

print("PPAP" if "".join(stack) == "P" else "NP")