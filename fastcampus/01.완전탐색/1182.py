import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def rec(depth, result):
    global cnt
    if depth >= n:
        if result == s:
            cnt += 1
        return
    else:
        rec(depth + 1, result + arr[depth])
        rec(depth + 1, result)

rec(0, 0)
if s == 0:
    cnt -= 1
print(cnt)
