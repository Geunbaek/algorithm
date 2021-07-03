import sys
input = sys.stdin.readline
# pypy

def expand(left, right):
    while left >= 0 and right < len(arr) and arr[left] == arr[right]:
        palin.add((left, right))
        left -= 1
        right += 1


n = int(input())
arr = list(map(int, input().split()))
palin = set()

for i in range(len(arr)):
    expand(i, i + 1)
    expand(i, i)

m = int(input())
for _ in range(m):
    start, end = map(int, input().split())
    if (start-1, end-1) in palin:
        print(1)
    else:
        print(0)
