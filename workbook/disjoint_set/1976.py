import sys

input = sys.stdin.readline

def find_p(x):
    if p[x] != x:
        p[x] = find_p(p[x])
    return p[x]

def union(a, b):
    ap = find_p(a)
    bp = find_p(b)
    p[ap] = bp

n = int(input())
p = [i for i in range(n+1)]

m = int(input())

for y in range(n):
    arr = list(map(int, input().split()))
    for x in range(n):
        if arr[x] == 1:
            union(x+1, y+1)

ans = []
country = list(map(int, input().split()))
for c in country:
    ans.append(find_p(c))

if len(set(ans)) == 1:
    print("YES")
else:
    print("NO")
