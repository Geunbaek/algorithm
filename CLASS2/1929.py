import sys
input = sys.stdin.readline

m, n = map(int, input().split())

arr = [True for i in range(n+1)]

for i in range(2, n+1):
    if arr[i]:
        if i >= m:
            print(i)
        num = i
        a = num
        while a + num <= n:
            a += num
            arr[a] = False
