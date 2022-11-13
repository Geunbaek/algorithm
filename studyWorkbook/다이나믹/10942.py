import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
palin = set()
dp = [[0 for _ in range(n)] for _ in range(n)]

count = 0
for x in range(n):
    for start in range(n):
        end = start + count
        if end >= n:
            break
        if start == end:
            dp[start][end] = 1
            continue

        if arr[start] == arr[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start + 1][end - 1] == 1:
                dp[start][end] = 1
    count += 1

m = int(input())
for _ in range(m):
    start, end = map(int, input().split())
    print(dp[start - 1][end - 1])

"""
7
1 1 1 1 1 1 1
4
1 3
2 5
3 3
5 7

[1, 1, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 1, 1, 1]
[0, 0, 1, 1, 1, 1, 1]
[0, 0, 0, 1, 1, 1, 1]
[0, 0, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 0, 1, 1]
[0, 0, 0, 0, 0, 0, 1]

"""

