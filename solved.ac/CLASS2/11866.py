import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i+1 for i in range(n)]
idx = 0
answer = []
while arr:
    idx += k-1
    idx %= len(arr)
    answer.append(arr.pop(idx))
if n == 1:
    print("<" + str(answer[0]) + ">")
else:
    for i in range(len(answer)):
        if i == 0:
            print("<" + str(answer[i]) +",", end = " ")
        elif i == len(answer)-1:
            print(str(answer[i]) + ">")
        else:
            print(str(answer[i])+",", end = " ")

