import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    apart = [[0] * (n+1) for i in range(k+1)]
    for i in range(k+1):
        for j in range(n+1):
            if i == 0:
                apart[i][j] = j
            else:
                apart[i][j] = sum(apart[i-1][:j+1])

    print(apart[-1][-1])
