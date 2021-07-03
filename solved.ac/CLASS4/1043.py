import sys
input = sys.stdin.readline

def find_p(x):
    if x != p[x]:
        p[x] = find_p(p[x])
    return p[x]

def union(a, b):
    ap = find_p(a)
    bp = find_p(b)
    if ap in trust:
        p[bp] = ap
    elif bp in trust:
        p[ap] = bp
    else:
        p[ap] = bp


n, m = map(int, input().split())

arr = list(map(int, input().split()))
trust_cnt, trust = arr[0], set(arr[1:])

p = [i for i in range(n+1)]
cnt = 0
check = []

for _ in range(m):
    arr2 = list(map(int, input().split()))
    participant_cnt, paricipant = arr2[0], arr2[1:]

    for a in paricipant[1:]:
        union(paricipant[0], a)
    check.append(paricipant)

for li in check:
    ck = False
    for i in li:
        if find_p(i) in trust:
            ck = True
            break
    if not ck:
        cnt += 1

print(cnt)

