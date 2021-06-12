import sys
input = sys.stdin.readline
import heapq

INF = 10**9

def sol():
    h = []
    visit = [INF] * 100001
    for i in (n+1, n-1, n*2):
        heapq.heappush(h, (1, i))

    results = []

    while h:
        t, now = heapq.heappop(h)
        if 0 <= now < 100001 and visit[now] >= t:
            visit[now] = t
            if now == k:
                results.append(t)
            for i in (now + 1, now - 1, now * 2):
                heapq.heappush(h, (t+1, i))
    return results

n, k = map(int, input().split())

if n == k:
    print(0)
    print(1)
    exit()
if n > k:
    print(n-k)
    print(1)
    exit()

ans = sol()
print(min(ans))
print(ans.count(min(ans)))


