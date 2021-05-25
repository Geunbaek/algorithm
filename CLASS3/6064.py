import sys
input = sys.stdin.readline
# pypy
t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    x1, y1 = x, x
    while x1 > m:
        x1 -= m
    while y1 > n :
        y1 -= n
    cnt = x
    visit = set()
    if x1 == x and y1 == y:
        print(cnt)
    else:
        while y1 not in visit:
            visit.add(y1)
            y1 += m
            while y1 > n:
                y1 -= n
            cnt += m
            if y1 == y:
                visit.add(y1)
                break
        if y not in visit:
            print(-1)
        else:
            print(cnt)





