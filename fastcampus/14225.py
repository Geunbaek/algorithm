import sys
input = sys.stdin.readline

def recur(depth, val):
    if depth >= len(arr):
        sums.add(val)
        return
    if val:
        sums.add(val)
    for i in range(depth, len(arr)):
        if visit[i] == 0:
            visit[i] = 1
            recur(i + 1, val + arr[i])
            visit[i] = 0


n = int(input())
arr = list(map(int, input().split()))
sums = set()
visit = [0 for _ in range(len(arr))]

recur(0, 0)
for i in range(1, 100_000 * 20 + 1):
    if i not in sums:
        print(i)
        break