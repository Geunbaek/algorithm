import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input().strip())

    arr.sort()
    for i in range(n - 1):
        if arr[i + 1].startswith(arr[i]):
            print("NO")
            break
    else:
        print("YES")