import sys
input = sys.stdin.readline

def recur(now, cnt, path):
    if cnt >= m:
        print(*path)
        return

    for i in range(now, n+1):
        if visit[i] == 0:
            visit[i] = 1
            recur(i, cnt + 1, path + [i])
            visit[i] = 0

n, m = map(int, input().split())
visit = [0 for _ in range(n + 1)]
recur(1, 0, [])
