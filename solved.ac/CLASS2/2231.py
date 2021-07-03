import sys
input = sys.stdin.readline

n = int(input())
c = 0

for i in range(n+1):
    num = i
    for j in str(i):
        num += int(j)
    if num == n:
        c = i
        break
print(c)
