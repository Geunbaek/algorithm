import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [0 for _ in range(n + 1)]
    ck = [0 for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[b] = a

    a, b = map(int, input().split())
    now = a

    while now:
        ck[now] = 1
        now = graph[now]

    now = b
    while now and ck[now] == 0:
        now = graph[now]
    print(now)


