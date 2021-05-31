import sys
input = sys.stdin.readline

n, m = map(int, input().split())
web_password = {}

for _ in range(n):
    w, p = input().strip().split()
    web_password[w] = p

for _ in range(m):
    w = input().strip()
    print(web_password[w])