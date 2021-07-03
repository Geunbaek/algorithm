import sys

input = sys.stdin.readline
num = set()
for _ in range(10):
    num.add(int(input())%42)

print(len(num))