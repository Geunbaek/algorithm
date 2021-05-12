import sys
input = sys.stdin.readline

n = int(input())
arr = []
answer = []
is_availble = True

for _ in range(n):
    num = int(input())
    arr.append(num)

stack = []
idx = 1
while arr:
    if not stack:
        stack.append(idx)
        idx += 1
        answer.append('+')

    if arr[0] < idx and stack[-1] != arr[0]:
        is_availble = False
        break

    while arr[0] >= idx:
        stack.append(idx)
        answer.append("+")
        idx +=1

    while stack and arr[0] == stack[-1]:
        arr.pop(0)
        stack.pop()
        answer.append("-")

if not is_availble:
    print("NO")
else:
    for i in answer:
        print(i)




