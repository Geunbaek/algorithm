import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
p = [0 for _ in range(n)]

n_a = []
for idx, el in enumerate(a):
    n_a.append([idx, el])
b = []

for idx, el in enumerate(sorted(n_a, key = lambda x:x[1])):
    b.append(el)

for idx, el in enumerate(a):
    p[idx] = b.index([idx, el])

for el in p:
    print(el, end = ' ')
