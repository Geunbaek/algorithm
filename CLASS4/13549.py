import sys
input = sys.stdin.readline
import heapq

INF = 10**9
def sol():
    h = []
    heapq.heappush(h, (0, n))
    visit = [INF]*100001
    while h:
        time, now = heapq.heappop(h)
        if now == k:
            return time
        for i in (now+1, now-1):
            if 0 <= i <= 100000 and visit[i] > time:
                visit[i] = time+1
                heapq.heappush(h, (time+1, i))
        for i in (now*2,):
            if 0 <= i <= 100000 and visit[i] > time:
                visit[i] = time
                heapq.heappush(h, (time,i))

n, k = map(int, input().split())

print(sol())